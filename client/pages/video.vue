<video id=example-video width=960 height=540 class="video-js vjs-default-skin" controls>
  <source
     src="https://example.com/index.m3u8"
     type="application/x-mpegURL">
</video>
<script src="video.js"></script>
<script src="videojs.hls.min.js"></script>
<script>
var player = videojs('example-video');
player.play();
</script>
