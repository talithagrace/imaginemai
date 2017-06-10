import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map';

/*
  Generated class for the PeopleServiceProvider provider.

  See https://angular.io/docs/ts/latest/guide/dependency-injection.html
  for more info on providers and Angular 2 DI.
*/
@Injectable()
export class PeopleService {
  data1: any;
  constructor(public http: Http) {
    console.log('Hello PeopleService Provider');
  }

  load() {
    if (this.data1) {
      return Promise.resolve(this.data1);
      }
      //dont have the data yet
      return new Promise(resolve => {
        this.http.get('https://imaginemai.herokuapp.com/api/posts/')
          .map(res => res.json())
          .subscribe(data => {
            this.data1 = data;
            resolve(this.data1);
          });
      });
    }

}
