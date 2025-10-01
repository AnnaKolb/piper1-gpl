export OMP_NUM_THREADS=1
rm -rf ./cache_fresh
python -m piper.train fit \
  --data.voice_name "HomeBrewed Arabic Voice" \
  --data.csv_path ../corpus/metadata.csv \
  --data.audio_dir ../corpus/wavs \
  --data.espeak_voice "en-us" \
  --model.sample_rate 22050 \
  --data.cache_dir ./cache_fresh \
  --data.config_path ./cache_fresh/config.json \
  --data.batch_size 1 \
  --data.num_workers 0 \
  --trainer.accelerator cpu \
  --trainer.max_epochs 3000 \
  --trainer.num_sanity_val_steps 0 \
  --ckpt_path ../piper-checkpoints/en/en_US/lessac/medium/epoch=2164-step=1355540.ckpt



