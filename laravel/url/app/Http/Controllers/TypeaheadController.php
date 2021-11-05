<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class TypeaheadController extends Controller
{

    public function autocompleteSearch(Request $request)
    {
          $query = $request->get('query');
          $filterResult = DB::table("url")->where('url', 'LIKE', '%'. $query. '%')->get();
          return response()->json($filterResult);
    }
}
