new Vue({
    el: '#post_app',
    data: {
    posts: []
    },

    created: function() {
        const vm = this;
        axios.get('/api/blog/')
        .then(function(response){
        vm.posts = response.data
        })
    }
}
)