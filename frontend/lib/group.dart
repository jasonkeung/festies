import 'dart:convert';
import 'dart:io';

import 'package:flutter/widgets.dart';
import 'package:http/http.dart' as http;
import 'package:flutter/material.dart';

const String localUrl = 'http://127.0.0.1:5000/groups';

class GroupCardList extends StatefulWidget {
  const GroupCardList({super.key});

  @override
  State<StatefulWidget> createState() {
    return _GroupCardListState();
  }
}

class _GroupCardListState extends State<GroupCardList> {
  late Future<List<Group>> futureGroups;
  @override
  void initState() {
    super.initState();
    futureGroups = fetchGroups();
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
        future: futureGroups,
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            return ListView.separated(
                itemBuilder: (BuildContext context, int index) {
                  return Container(
                    height: 50,
                    child: Text(snapshot.data![index].groupBio),
                  );
                },
                separatorBuilder: (BuildContext context, int index) =>
                    const Divider(),
                itemCount: snapshot.data!.length);
          } else {
            return const Text('never got the groups');
          }
        });
  }
}

class Group {
  final String groupBio;

  const Group({required this.groupBio});

  factory Group.fromJson(Map<String, dynamic> json) {
    return Group(groupBio: json['group_bio']);
  }
}

Future<List<Group>> fetchGroups() async {
  // final client = HttpClient();
  // final request = await client.getUrl(Uri.parse(localUrl));
  // final response = await request.close();

  final response = await http.get(Uri.parse(localUrl));
  if (response.statusCode == 200) {
    List<dynamic> groupJsons = json.decode(response.body);
    List<Group> groups =
        groupJsons.map((gJson) => Group.fromJson(gJson)).toList();
    return groups;
  } else {
    return [
      Group.fromJson({"group_bio": 'got a bad response'})
    ];
  }
}
