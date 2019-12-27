Title: Notes
Slug: notes

This is where I'm storing notes for things I seldom use and often need

* ffmpeg for video to gif for this site: `ffmpeg -i file.mov -filter:v scale=1000:-1 -pix_fmt rgb24 -r 10 -f gif - | gifsicle --optimize=3 > file.gif`