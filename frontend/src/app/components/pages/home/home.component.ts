import { Component } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { IUser } from 'src/app/interface/User';
import { UserService } from 'src/app/services/user.service';
import { ModalComponent } from '../../modal/modal.component';

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
  selectedNewContact = 'email'
  newUser = INITIAL_USER

  isEdit = false
  editUser!: IUser

  constructor(private userService: UserService, private modalService: NgbModal) {
    this.getAllUsers()
  }

  getAllUsers(): void {
    this.userService
      .getAllUsers()
      .subscribe((users) => this.users = users)
  }  

  onCreateUser(user: IUser): void {
    this.userService
      .createUser(user)
      .subscribe((response) => {
        this.users = [...this.users, response.data]
        this.newUser = {
          _id: '',
          name: '',
          contacts: [{ type: 'email', contact: ''}]
        }
      })  
  }

  onEditUser(user: IUser): void {
    this.isEdit = true
    this.editUser = user
  }

  deleteContactOnCreateUser(index: number): void {
    this.newUser.contacts.splice(index, 1)
  }

  onSaveUser(user: IUser): void {
    this.userService
      .putUser(user)
      .subscribe(() => {
        this.isEdit = false
        this.editUser = INITIAL_USER
      })
  }

  onRemoveUser(user: IUser): void {
    this.openModal(user)
  }

  handleSelectedNewContact({ target }: any): void {
    const { value } = target
    
    this.selectedNewContact = value
  }

  addContactOnCreateUser(): void {
    this.newUser = { ...this.newUser, contacts: [...this.newUser.contacts, { type: this.selectedNewContact, contact: ''} ]}
  }

  addContactOnEdit(): void {
    this.editUser.contacts = [...this.editUser.contacts, { type: this.selectedNewContact, contact: ''} ]
  }

  deleteContactOnEdit(index: number): void {
    this.editUser.contacts.splice(index, 1)
  }

  openModal(user: IUser): void {
    const modalRef = this.modalService.open(ModalComponent)
    modalRef.componentInstance.user = user
    modalRef.dismissed.subscribe(() => {
      if (user._id) 
        this.userService
            .deleteUser(user._id)
            .subscribe(() => this.users = this.users.filter((u) => u._id !== user._id))
    })
  }
}
