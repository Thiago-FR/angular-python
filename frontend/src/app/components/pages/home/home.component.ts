import { Component } from '@angular/core';
import { IUser } from 'src/app/interface/User';
import { UserService } from 'src/app/services/user.service';

const INITIAL_USER = {
  _id: '',
  name: '',
  contacts: [{ type: 'email', contact: ''}]
}

const TYPES_CONTACTS = {
  email: "Email",
  cell: "Celular",
  homePhone: "Telefone Residencial"
} as any

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent {
  users: IUser[] = []

  typeContacts = TYPES_CONTACTS
  selectedNewContact = TYPES_CONTACTS.email
  newUser = INITIAL_USER

  isEdit = false
  editUser!: IUser

  constructor(private userService: UserService) {
    this.getAllUsers()
  }

  onEdit(user: IUser): void {
    this.isEdit = true
    this.editUser = user
  }

  onCreateuser(user: IUser): void {
    this.userService
      .createUser(user)
      .subscribe((response) => {
        this.users = [...this.users, response.data]
        this.newUser = INITIAL_USER
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
      .subscribe(() => {
        this.isEdit = false
        this.editUser = INITIAL_USER
      })
  }

  onRemove(user: IUser): void {
    if (user._id) this.userService
      .deleteUser(user._id)
      .subscribe(() => this.users = this.users.filter((u) => u._id !== user._id))
  }

  handleSelectedNewContact({ target }: any): void {
    const { value } = target
    
    this.selectedNewContact = value
  }

  addContact(): void {    
    this.newUser = { ...this.newUser, contacts: [...this.newUser.contacts, { type: this.selectedNewContact, contact: ''} ]}
  }

  lof(any: any) {
    console.log(any)
  }
}
