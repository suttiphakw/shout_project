const app = Vue.createApp({
    data() {
        return {
            instagramIsVisible: true,
            igFbShareIsVisible: true,
            tiktokIsVisible: true,
            twitterIsVisible: true,
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