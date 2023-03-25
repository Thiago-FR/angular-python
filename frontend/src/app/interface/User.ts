interface IContactType { type: string, contact: string }

export interface IUser {
    _id?: string,
    name: string,
    contacts: Array<IContactType>
}