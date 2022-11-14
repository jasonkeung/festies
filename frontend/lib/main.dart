import 'package:flutter/material.dart';

import 'group.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  static const String _title = 'Festies';

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: _title,
      home: const HomePage(),
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        brightness: Brightness.light,
        primaryColor: Colors.blueGrey,
      ),
    );
  }
}

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: const Center(
        child: GroupCardList(),
      ),
      appBar: AppBar(title: const Text('test')),
    );
  }
}
