@extends('layouts.conapp')

<body style="background: #f6f5fa;">

<!--content S-->
@if(isset($res))
    　　<div class="alert alert-success alert-dismissable" role="alert">
        <button type="button" class="close" data-dismiss="alert"
                aria-hidden="true">
            &times;
        </button>
        　　　　{{$res}}
        　　</div>
@endif
<div class="super-content RightMain" id="RightMain">

    <!--header-->
    <div class="superCtab">
        <div class="tp-title clearfix">
            <h3>拍照</h3>
        </div>

        <div class="ctab-Main">
@if(isset($ret))
                <div class="ctab-Mian-cont" >
                    <a href="/capture?act=1">
                        <input style="text-align: center;margin-top: 5vh;margin-left: 35vw"
                               type="submit" id="myButton"
                               class="btn btn-primary" autocomplete="off" value="再次拍照">

                    </a>
                    <div style="text-align: center">
                        <img class=""
                             src="data:image/jpeg;base64,{{base64_encode($ret->face_path)}}"
                             alt="{{$ret->face_name1}}{{$ret->face_name2}}" height="350px"
                             style="padding: 4px;background-color: #fff;border: 1px solid #ddd;border-radius: 4px;">
                        <br><span>{{$ret->face_name1}}{{$ret->face_name2}}</span>
                    </div>
                </div>
            @else
            <div class="ctab-Mian-cont" >
                <a href="/capture?act=1">
                    <input style="text-align: center;margin-top: 35vh;margin-left: 35vw"
                           type="submit" id="myButton"
                           class="btn btn-primary" autocomplete="off" value="拍照">

                </a>
            </div>
    @endif

        </div>

    </div>
</div>


</body></html>