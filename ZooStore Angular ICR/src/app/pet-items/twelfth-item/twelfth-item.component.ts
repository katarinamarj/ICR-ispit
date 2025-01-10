import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-twelfth-item',
  templateUrl: './twelfth-item.component.html',
  styleUrl: './twelfth-item.component.css'
})
export class TwelfthItemComponent {

  product = {
    id: 12,
    name: 'Cuddles',
    price: 35,
    type: 'Rabbit',
    color: 'Gray',
    age: '2',
    size: 'Small',
    origin: 'Germany',
    review: '4 stars',
    image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRI-a4PNsfOOfJcgEiDfL3QJ5t6NzP8COK_ghmWyG431p6OQz4-V2zUmKfgnAectbgIYXc&usqp=CAU'
  };


  constructor(
    private cartService: CartService,  
    private router: Router  
  ) {}

  addToCart(product: any) {
    this.cartService.addToCart(product);  
    alert('Product added to cart!');
    this.router.navigate(['/cart']); 
  }
}
