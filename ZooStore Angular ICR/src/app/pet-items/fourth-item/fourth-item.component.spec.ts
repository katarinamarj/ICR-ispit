import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FourthItemComponent } from './fourth-item.component';

describe('FourthItemComponent', () => {
  let component: FourthItemComponent;
  let fixture: ComponentFixture<FourthItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [FourthItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FourthItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
