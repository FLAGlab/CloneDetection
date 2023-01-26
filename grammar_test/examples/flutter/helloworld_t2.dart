import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? akey}) : super(key: akey);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    final x = 3; //new variable added
    String s;
    s = 'Hello Flutter';
    return MaterialApp(
      title: 'Flutter Demo',
      home: Scaffold(
          appBar: AppBar( title: const Text('Welcome to flutter'),),
          body: Center( child: Text(s),)
      ),
    );
  }
}
