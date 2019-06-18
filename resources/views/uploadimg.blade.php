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
@if(!empty(session('warning')))
    　　<div class="alert alert-warning alert-dismissable" role="alert">
        <button type="button" class="close" data-dismiss="alert"
                aria-hidden="true">
            &times;
        </button>
        　　　　{{session('warning')}}
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
<div class="super-content RightMain" id="RightMain">
    <div class="superCtab">
        <div class="ctab-title clearfix">
            <h3>照片上传</h3>
        </div>
    </div>
    <form action="{{url('upload_img')}}" method="post" enctype="multipart/form-data">
        <div class="form-group" style="margin-top: 20vh;margin-left: 40vw">
            请选择文件：
            <input type="file" id="exampleInputFile" name="upimg" ><br>
            <input type="submit" class="btn btn-default">Submit</input>
        </div>
    </form>
</div>


</body>
</html>