import 'package:crypto_client/providers/funds.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:provider/provider.dart';

class InvitationScreen extends StatefulWidget {
  final int fund;
  InvitationScreen({Key? key, required this.fund}) : super(key: key);

  @override
  _InvitationScreenState createState() => _InvitationScreenState();
}

class _InvitationScreenState extends State<InvitationScreen> {
  String username = "";
  final formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Invitation'),
        actions: <Widget>[
          TextButton(
            child: const Text('Funds', style: TextStyle(color: Colors.white)),
            onPressed: () {
              Navigator.pushReplacementNamed(context, '/funds');
            },
          ),
          IconButton(
            icon: Icon(Icons.logout),
            onPressed: () {
              Navigator.pushReplacementNamed(context, '/login');
            },
          ),
        ],
      ),
      body: Center(
          child: SizedBox(
        height: MediaQuery.of(context).size.height * 0.4,
        width: MediaQuery.of(context).size.width * 0.8,
        child: Form(
          key: formKey,
          child: Column(
            children: [
              TextFormField(
                decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                  labelText: 'Username',
                ),
                onChanged: (value) {
                  setState(() {
                    username = value;
                  });
                },
              ),
              ElevatedButton(
                child: const Text('Invite'),
                onPressed: () async {
                  if (formKey.currentState!.validate()) {
                    int statusCode =
                        await Provider.of<FundsProvider>(context, listen: false)
                            .inviteUserToFund(
                                username: username, fund: widget.fund);
                    Navigator.of(context).pop();
                  }
                },
              ),
            ],
          ),
        ),
      )),
    );
  }
}
