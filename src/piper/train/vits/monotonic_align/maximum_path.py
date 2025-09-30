import numpy as np
import torch

def maximum_path(neg_cent: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
    """
    Pure NumPy fallback (safe on macOS; slower but avoids Cython segfaults).
      neg_cent: [B, T, S] float
      mask:     [B, T, S] bool/int
    returns:    [B, T, S] same dtype/device as neg_cent
    """
    device = neg_cent.device
    out_dtype = neg_cent.dtype

    v = neg_cent.detach().to("cpu", dtype=torch.float32).numpy()
    v = np.nan_to_num(v, nan=-1e9, posinf=1e9, neginf=-1e9)
    B, T, S = v.shape

    t_ys = mask.sum(1)[:, 0].detach().to("cpu", dtype=torch.int32).numpy()
    t_xs = mask.sum(2)[:, 0].detach().to("cpu", dtype=torch.int32).numpy()
    t_ys = np.clip(t_ys, 1, T).astype(np.int32, copy=False)
    t_xs = np.clip(t_xs, 1, S).astype(np.int32, copy=False)

    paths = np.zeros((B, T, S), dtype=np.int32)

    for b in range(B):
        ty, tx = int(t_ys[b]), int(t_xs[b])
        val = np.full((ty, tx), -1e9, dtype=np.float32)

        for y in range(ty):
            minx = max(0, y - (ty - tx))
            maxx = min(tx, y + 1)
            for x in range(minx, maxx):
                if y == 0 and x == 0:
                    v_prev = 0.0
                elif x > 0 and y > 0:
                    v_prev = val[y-1, x-1]
                else:
                    v_prev = -1e9
                v_cur = -1e9 if x == y else (val[y-1, x] if y > 0 else -1e9)
                val[y, x] = v[b, y, x] + max(v_prev, v_cur)

        x = tx - 1
        for y in range(ty - 1, -1, -1):
            paths[b, y, x] = 1
            if x != 0 and (x == y or (y > 0 and val[y-1, x] < val[y-1, x-1])):
                x -= 1

    return torch.from_numpy(paths).to(device=device, dtype=out_dtype)
