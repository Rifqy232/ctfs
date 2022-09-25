package defpackage;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;

/* compiled from: Binarypin.java */
/* renamed from: ResetButton  reason: default package */
/* loaded from: Binary-Pin.jar:ResetButton.class */
class ResetButton extends JButton implements ActionListener {
    private Binarypin app;

    /* JADX INFO: Access modifiers changed from: package-private */
    public ResetButton(Binarypin binarypin, int i, int i2, int i3, int i4) {
        super("Reset");
        this.app = binarypin;
        addActionListener(this);
        setBounds(i, i2, i3, i4);
    }

    public void actionPerformed(ActionEvent actionEvent) {
        Secret.getInstance().resetInstance();
        this.app.clearOutput();
    }
}