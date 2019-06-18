<?php

namespace App\Http\Controllers;

//use Faker\Provider\Image;
use Illuminate\Http\Request;
//use Intervention\Image\ImageManager;
use Intervention\Image\ImageManagerStatic as Image;
use App\Http\Controllers\func;

class UploadimgController extends Controller
{
    //
    public function index()
    {
        return view("uploadimg");
    }

    public function upload(Request $request)
    {
//        dump($request);
//        dump($request->file('upimg'));
        if ($request->hasFile('upimg')) {
            $file = $request->file('upimg');
            //$file=Image::
            $file = Image::make($file)->resize(800,null, function($constraint){
                $constraint->aspectRatio();});
            $file->save(env('IMAGE_SAVE_PATH'));
            //$re=func::locapi('upload',env('IMAGE_SAVE_PATH'));
            if(-1!=$ret=func::locapi('upload',"/www/wwwroot/millyface.dlinks.cn/public/".env('IMAGE_SAVE_PATH')))
            {
                if($ret==1)
                return back()->with('success',"上传成功");
                else
                    return back()->with('warning',"未检测到或检测到多张人脸，请重新上传");
            }
        }
        return back()->with('fail',"服务器连接失败,请联系管理员");
    }
}
