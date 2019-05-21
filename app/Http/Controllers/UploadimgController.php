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
            $file = Image::make($file)->resize(200,null, function($constraint){
                $constraint->aspectRatio();});
            $file->save(env('IMAGE_SAVE_PATH'));
            //$re=func::locapi('upload',env('IMAGE_SAVE_PATH'));
            if(0==func::locapi('upload',env('IMAGE_SAVE_PATH')))
            return back()->with('success',"上传成功");
        }
        return back()->with('fail',"上传失败".$re);
    }
}
