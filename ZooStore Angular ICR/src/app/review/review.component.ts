import { Component, OnInit } from '@angular/core';
import { CartService } from '../cart.service'; 

@Component({
  selector: 'app-review',
  templateUrl: './review.component.html',
  styleUrls: ['./review.component.css']
})
export class ReviewComponent implements OnInit {

  reviews: any[] = []; 

  constructor(private cartService: CartService) { }

  ngOnInit() {
    this.reviews = this.cartService.getReviews(); 
  }
}
