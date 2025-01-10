import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SecondItemComponent } from './second-item.component';

describe('SecondItemComponent', () => {
  let component: SecondItemComponent;
  let fixture: ComponentFixture<SecondItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SecondItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SecondItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
