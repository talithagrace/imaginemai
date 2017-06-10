import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import {PeopleService} from '../../providers/people-service/people-service';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html',
  providers: [PeopleService]
})
export class HomePage {
  public posts: any;
  constructor(public navCtrl: NavController, public peopleService: PeopleService) {
    this.loadPosts();
  }

  loadPosts() {
    this.peopleService.load()
      .then(data1 => {
        this.posts = data1;
      })

    }

}
