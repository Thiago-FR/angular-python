import { Component, Input } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { IModal } from 'src/app/interface/Modal';
import { IUser } from 'src/app/interface/User';


@Component({
  selector: 'app-modal',
  templateUrl: './modal.component.html',
  styleUrls: ['./modal.component.css']
})
export class ModalComponent {
  @Input() user!: IUser
  @Input() modal!: IModal

  constructor(public activeModal: NgbActiveModal) {}
}
