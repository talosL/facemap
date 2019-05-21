@extends('layouts.app')

@section('content')
    <div class="superWrap clearfix" style="height: 100%;">
        <!--side S-->
        <div class="super-side-menu">
            <div class="super-side-menu">
                <iframe src="{{url('sidebar')}}" width="205" height="100%" marginheight="0" marginwidth="0" frameborder="0" scrolling="no"></iframe>
            </div>
        </div>
        <!--side E-->
        <!--content S-->
        <div class="superContent">
            <div class="superCtab superCtabBot" style="height: 695px;">
                <iframe src="{{url('today_ac')}}" id="Mainindex" name="Mainindex" width="100%" height="100%" marginheight="0" marginwidth="0" frameborder="0"></iframe>
            </div>
            <!--main-->

        </div>
        <!--content E-->

    </div>
    <script>
        window.onresize = function(){
            var winH=$(window).height();
            var headH=$('.super-header').height();
            $('.superWrap').height(winH);
            $('.superCtabBot').height(winH-headH);
        };
        $(window).resize();
    </script>
@endsection
