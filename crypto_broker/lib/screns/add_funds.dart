import 'package:crypto_client/providers/funds.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:provider/provider.dart';

// A widget that has form (with following fields: String name, int totaValue and double fee), and a button to submit the form.
class AddFundsScreen extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _AddFundsScreenState();
  }
}

class _AddFundsScreenState extends State<AddFundsScreen> {
  final _formKey = GlobalKey<FormState>();
  String _name = '';
  double _fee = 0.0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Container(
          padding: EdgeInsets.all(30.0),
          child: Form(
            key: _formKey,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: <Widget>[
                TextFormField(
                  decoration: const InputDecoration(labelText: 'Name'),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please input your name';
                    }
                    return null;
                  },
                  onChanged: (value) {
                    setState(() {
                      _name = value;
                    });
                  },
                ),
                TextFormField(
                  decoration: const InputDecoration(labelText: 'Fee'),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please input your fee';
                    }
                    if (double.tryParse(value) == null) {
                      return 'Please input a positive number';
                    }
                    if (double.parse(value) < 0) {
                      return 'Please input a positive number';
                    }
                    if (double.parse(value) > 100) {
                      return 'Please input a number less than 100';
                    }
                    return null;
                  },
                  onChanged: (value) {
                    setState(() {
                      _fee = double.parse(value);
                    });
                  },
                ),
                Padding(
                  padding: const EdgeInsets.symmetric(vertical: 16.0),
                  child: ElevatedButton(
                    onPressed: () async {
                      if (_formKey.currentState!.validate()) {
                        final statusCode = await Provider.of<FundsProvider>(
                                context,
                                listen: false)
                            .createFund(
                          fee: _fee,
                          name: _name,
                        );
                        if (statusCode == 201) {
                          Navigator.pop(context);
                        }
                      }
                    },
                    child: const Text('Submit'),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
