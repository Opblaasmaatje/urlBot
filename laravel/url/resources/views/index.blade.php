<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- CSRF Token -->
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <title>{{ config('app.name', 'Laravel') }}</title>
    <link rel="icon" href="{{ url('css/favicon.png') }}">
    <script src="{{ asset('js/app.js') }}" defer></script>
    <link rel="dns-prefetch" href="//fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css?family=Nunito" rel="stylesheet">
    <link href="{{ asset('css/app.css') }}" rel="stylesheet">
</head>

<body>
    <div class="container">
        <nav class="navbar navbar-light bg-light justify-content-between">
            <a class="navbar-brand">LinkDetector Bot</a>
        </nav>
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">url</th>
                </tr>
            </thead>
            <tbody>
                @foreach ($urls as $url)
                    <tr>
                        <td>{{ $url->id }}</td>
                        <td>{{ $url->url }}</td>
                    </tr>
                @endforeach
            </tbody>
        </table>
    </div>
</body>




</html>
