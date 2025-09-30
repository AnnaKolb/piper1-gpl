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
  --trainer.num_sanity_val_steps 0
