import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SixthItemComponent } from './sixth-item.component';

describe('SixthItemComponent', () => {
  let component: SixthItemComponent;
  let fixture: ComponentFixture<SixthItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SixthItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SixthItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
