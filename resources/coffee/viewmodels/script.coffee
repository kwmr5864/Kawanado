searchFormVm = new Vue({
    el: '#searchForm',
    data: {
        keyword: '',
        alert:
            enable: false,
            class: {},
            type: '',
            message: '',
    },
    methods: {
        setClass: (success, danger) ->
            this.alert.class = {
                'alert-success': success,
                'alert-danger': danger,
            }
        isBlank: (s) ->
            return !s? || s.trim?() is ''
        search: ->
            this.alert.enable = true
            this.setClass false, false
            if this.isBlank this.keyword
                this.setClass false, true
                this.alert.type = 'エラー: '
                this.alert.message = '入力が空です'
            else
                this.setClass true, false
                this.alert.type = 'Success'
                this.alert.message = ''
                that = this
                setTimeout(() ->
                    that.$el.submit()
                , 1000)
    },
})
