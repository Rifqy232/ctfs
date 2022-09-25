package defpackage;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;

/* compiled from: Binarypin.java */
/* renamed from: PinButton  reason: default package */
/* loaded from: Binary-Pin.jar:PinButton.class */
class PinButton extends JButton implements ActionListener {
    Binarypin app;

    /* JADX INFO: Access modifiers changed from: package-private */
    public PinButton(Binarypin binarypin, String str, int i, int i2, int i3, int i4) {
        super(str);
        this.app = binarypin;
        addActionListener(this);
        setBounds(i, i2, i3, i4);
    }

    public void actionPerformed(ActionEvent actionEvent) {
        Secret.getInstance().process(getText().charAt(0));
        this.app.updateOutput();
    }
}