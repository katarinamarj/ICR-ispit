import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NineteenthItemComponent } from './nineteenth-item.component';

describe('NineteenthItemComponent', () => {
  let component: NineteenthItemComponent;
  let fixture: ComponentFixture<NineteenthItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [NineteenthItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NineteenthItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
