const app = Vue.createApp({
    data() {
        return {
            instagramIsVisible: true,
            igFbShareIsVisible: true,
            tiktokIsVisible: false,
            twitterIsVisible: false,
            // message: 'Hello Vue',
        };
    },
    methods: {
        instagramToggle() {
            this.instagramIsVisible = !this.instagramIsVisible;
        },
        igFbShareToggle() {
            this.igFbShareIsVisible = !this.igFbShareIsVisible;
        },
        tiktokToggle() {
            this.tiktokIsVisible = !this.tiktokIsVisible;
        },
        twitterToggle() {
            this.twitterIsVisible = !this.twitterIsVisible;
        },
    }
});

app.mount('#choose_social');

function showPreview1(event){
  if(event.target.files.length > 0){
    var src = URL.createObjectURL(event.target.files[0]);
    var preview = document.getElementById("file-ip-1-preview");
    preview.src = src;
    preview.style.display = "block";
  }
}

function showPreview2(event){
  if(event.target.files.length > 0){
    var src = URL.createObjectURL(event.target.files[0]);
    var preview = document.getElementById("file-ip-2-preview");
    preview.src = src;
    preview.style.display = "block";
  }
}

