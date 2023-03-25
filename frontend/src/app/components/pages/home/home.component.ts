import { Component } from '@angular/core';
import { IUser } from 'src/app/interface/User';
import { UserService } from 'src/app/services/user.service';

const INITIAL_USER = {
  user: {} as IUser,
  isEdit: false
}

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  users: IUser[] = []
  editUser = INITIAL_USER
  newUser = {} as IUser

  constructor(private userService: UserService) {
    this.getAllUsers()
  }

  onEdit(user: IUser): void {
    this.editUser = {
      user,
      isEdit: true
    }
  }

  onCreateuser(user: IUser): void {
    this.userService
      .createUser(user)
      .subscribe((response) => {
        this.users = [...this.users, response.data]
        this.newUser = {} as IUser
      })
  }

  getAllUsers(): void {
    this.userService
      .getAllUsers()
      .subscribe((users) => this.users = users)
  }

  onSaveUser(user: IUser): void {
    this.userService
      .putUser(user)
      .subscribe(() => this.editUser = INITIAL_USER)
  }

  onRemove(user: IUser): void {
    if (user._id) this.userService
      .deleteUser(user._id)
      .subscribe(() => this.users = this.users.filter((u) => u._id !== user._id))
  }
}
