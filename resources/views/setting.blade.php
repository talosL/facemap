@extends('layouts.conapp')

<body style="background: #f6f5fa;">
@if(!empty(session('success')))
    　　<div class="alert alert-success alert-dismissable" role="alert">
        <button type="button" class="close" data-dismiss="alert"
                aria-hidden="true">
            &times;
        </button>
        　　　　{{session('success')}}
        　　</div>
@endif
@if(!empty(session('fail')))
    　　<div class="alert alert-danger  alert-dismissable" role="alert">
        <button type="button" class="close" data-dismiss="alert"
                aria-hidden="true">
            &times;
        </button>
        　　　　{{session('fail')}}
        　　</div>
@endif
<!--content S-->
<div class="super-content RightMain" id="RightMain">

    <!--header-->
    <div class="superCtab">
        <div class="tp-title clearfix">
            <h3>管理设置</h3>
        </div>

        <div class="ctab-Main" >

            <div class="ctab-Mian-cont" >
                <form action="{{url('delete_face')}}" method="get">
                <input style="text-align: center;margin-top: 35vh;margin-left: 35vw"
                       type="submit" id="myButton"
                       class="btn btn-primary" autocomplete="off" value="清除现有数据">

                </form>
            </div>
            </div>

        </div>

    </div>
</div>


</body></html>