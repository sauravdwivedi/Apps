import 'package:flutter/material.dart';
import 'api.dart';

void main() async {
  String time = 'NULL';
  String rate = 'NULL';

  Future apiCall() async {
    SekToInr apiCall = SekToInr(time: time, rate: rate);
    await apiCall.apiCall();
    time = apiCall.time;
    rate = apiCall.rate;
  }

  await apiCall();
  runApp(MyApp(time, rate));
}

class MyApp extends StatelessWidget {
  String _time = 'NULL';
  String _rate = 'NULL';

  MyApp(String time, String rate) {
    _time = time;
    _rate = rate;
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blueGrey,
      ),
      home: MyHomePage(_time, _rate),
    );
  }
}

class MyHomePage extends StatefulWidget {
  String _time = 'NULL';
  String _rate = 'NULL';

  MyHomePage(String time, String rate) {
    _time = time;
    _rate = rate;
  }

  @override
  State<MyHomePage> createState() => _MyAppState(_time, _rate);
}

class _MyAppState extends State<MyHomePage> {
  String _time = 'NULL';
  String _rate = 'NULL';

  _MyAppState(String time, String rate) {
    _time = time;
    _rate = rate;
  }

  Future apiCall() async {
    SekToInr apiCall = SekToInr(time: _time, rate: _rate);
    await apiCall.apiCall();
    _time = apiCall.time;
    _rate = apiCall.rate;
  }

  void _refresh() {
    setState(() {
      apiCall();
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SEK to INR Conversion',
      theme: ThemeData(
        primarySwatch: Colors.blueGrey,
      ),
      home: Scaffold(
          appBar: AppBar(
            title: const Text('SEK to INR Conversion'),
          ),
          body: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Text(
                  '1 SEK = $_rate INR\n',
                  style: Theme.of(context).textTheme.headline5,
                ),
                Text(
                  'at $_time',
                  style: Theme.of(context).textTheme.headline5,
                )
              ],
            ),
          ),
          floatingActionButton: FloatingActionButton(
            onPressed: _refresh,
            tooltip: 'Refresh',
            child: const Icon(Icons.refresh),
          )),
    );
  }
}
