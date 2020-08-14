/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import javax.swing.table.DefaultTableModel;
import java.sql.*;
import java.util.ArrayList;
import javax.swing.RowFilter;
import javax.swing.table.TableRowSorter;

/**
 *
 * @author Enes
 */
public class demo extends javax.swing.JFrame {

    DefaultTableModel model;
    /**
     * Creates new form demo
     */
    public demo() {
        initComponents();

        polulateTable();
    }
    public void polulateTable(){
        model = (DefaultTableModel)tblStudents.getModel();
        model.setRowCount(0);
        try{
            ArrayList<Students> students = getStudents();
            for (Students students1 : students){
                Object[] row = {
                        students1.getOgrenciNo(),
                        students1.getOgrenciAdi(),
                        students1.getMatematik(),
                        students1.getEdebiyat(),
                        students1.getTarih(),
                        students1.getCografya(),
                        students1.getDin(),
                        students1.getFelsefe(),
                        students1.getKimya(),
                        students1.getFizik(),
                        students1.getBiyoloji(),
                        students1.getPuan()};
                model.addRow(row);
            }
        }catch (SQLException e){

        }
    }



    public ArrayList<Students> getStudents() throws SQLException{
        Connection connection = null;
        DbHelper helper = new DbHelper();
        Statement statement = null;
        ResultSet resultSet;
        ArrayList<Students> students = null;

        try{
            connection = helper.getConnection();
            statement = connection.createStatement();
            resultSet = statement.executeQuery("SELECT*FROM students");
            students = new ArrayList<Students>();
            while (resultSet.next()){
                students.add(new Students(
                   resultSet.getInt("ogr_no"),
                   resultSet.getString("ogr_ad"),
                   resultSet.getDouble("mat"),
                   resultSet.getDouble("edeb"),
                   resultSet.getDouble("tar"),
                   resultSet.getDouble("cog"),
                   resultSet.getDouble("din"),
                   resultSet.getDouble("fel"),
                   resultSet.getDouble("kim"),
                   resultSet.getDouble("fiz"),
                   resultSet.getDouble("biyo"),
                   resultSet.getDouble("puan")
                ));
            }
        }catch (SQLException e){
            helper.showErrorMassage(e);
        }finally {
            statement.close();
            connection.close();
        }
        return students;
    }

    public ArrayList<Students> sirala() throws SQLException{
        Connection connection = null;
        DbHelper helper = new DbHelper();
        Statement statement = null;
        ResultSet resultSet;
        ArrayList<Students> students = null;

        try{
            connection = helper.getConnection();
            statement = connection.createStatement();
             String kolon = txtSirala.getText();
            String sql = "select * from students ORDER BY "+kolon+" DESC";
            resultSet = statement.executeQuery(sql);
            students = new ArrayList<Students>();
            while (resultSet.next()){
                students.add(new Students(
                        resultSet.getInt("ogr_no"),
                        resultSet.getString("ogr_ad"),
                        resultSet.getDouble("mat"),
                        resultSet.getDouble("edeb"),
                        resultSet.getDouble("tar"),
                        resultSet.getDouble("cog"),
                        resultSet.getDouble("din"),
                        resultSet.getDouble("fel"),
                        resultSet.getDouble("kim"),
                        resultSet.getDouble("fiz"),
                        resultSet.getDouble("biyo"),
                        resultSet.getDouble("puan")));

            }

        }catch (SQLException e){
            helper.showErrorMassage(e);
            lblMassage.setText("Kolon bulunamadı");
            try{
                ArrayList<Students> students2 = getStudents();

                for (Students students1 : students2){
                    Object[] row = {
                            students1.getOgrenciNo(),
                            students1.getOgrenciAdi(),
                            students1.getMatematik(),
                            students1.getEdebiyat(),
                            students1.getTarih(),
                            students1.getCografya(),
                            students1.getDin(),
                            students1.getFelsefe(),
                            students1.getKimya(),
                            students1.getFizik(),
                            students1.getBiyoloji(),
                            students1.getPuan()};
                    model.addRow(row);
                }
            }catch (SQLException ex){

            }
        }finally {
            statement.close();
            connection.close();
        }
        return students;

    }
    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jScrollPane1 = new javax.swing.JScrollPane();
        tblStudents = new javax.swing.JTable();
        lblArama = new javax.swing.JLabel();
        txtArama = new javax.swing.JTextField();
        lblOgrNo = new javax.swing.JLabel();
        txtOgrNo = new javax.swing.JTextField();
        lblOgrAd = new javax.swing.JLabel();
        txtOgrAd = new javax.swing.JTextField();
        lblMat = new javax.swing.JLabel();
        txtMat = new javax.swing.JTextField();
        lblEdeb = new javax.swing.JLabel();
        txtEdeb = new javax.swing.JTextField();
        lblTar = new javax.swing.JLabel();
        txtTar = new javax.swing.JTextField();
        lblCog = new javax.swing.JLabel();
        txtCog = new javax.swing.JTextField();
        lblDin = new javax.swing.JLabel();
        txtDin = new javax.swing.JTextField();
        lblFel = new javax.swing.JLabel();
        txtFel = new javax.swing.JTextField();
        lblKim = new javax.swing.JLabel();
        txtKim = new javax.swing.JTextField();
        lblFiz = new javax.swing.JLabel();
        txtFiz = new javax.swing.JTextField();
        lblBiyo = new javax.swing.JLabel();
        btnEkle = new javax.swing.JButton();
        txtBiyo = new javax.swing.JTextField();
        txtSil = new javax.swing.JTextField();
        btnSil = new javax.swing.JButton();
        lblMassage = new javax.swing.JLabel();
        txtSirala = new javax.swing.JTextField();
        btnSirala = new javax.swing.JButton();
        lblPuan = new javax.swing.JLabel();
        txtPuan = new javax.swing.JTextField();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setBackground(new java.awt.Color(204, 204, 204));

        tblStudents.setBorder(javax.swing.BorderFactory.createEtchedBorder(java.awt.Color.white, java.awt.Color.darkGray));
        tblStudents.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {

            },
            new String [] {
                "ogr_no", "ogr_ad", "Matematik", "Edebiyat", "Tarih", "Coğrafya", "Din Kültür", "Felsefe", "Kimya", "Fizik", "Biyoloji", "Puan"
            }
        ) {
            Class[] types = new Class [] {
                java.lang.Integer.class, java.lang.String.class, java.lang.Double.class, java.lang.Double.class, java.lang.Double.class, java.lang.Double.class, java.lang.Double.class, java.lang.Double.class, java.lang.Double.class, java.lang.Double.class, java.lang.Double.class, java.lang.Double.class
            };
            boolean[] canEdit = new boolean [] {
                false, false, false, false, false, false, false, false, false, false, false, false
            };

            public Class getColumnClass(int columnIndex) {
                return types [columnIndex];
            }

            public boolean isCellEditable(int rowIndex, int columnIndex) {
                return canEdit [columnIndex];
            }
        });
        jScrollPane1.setViewportView(tblStudents);
        if (tblStudents.getColumnModel().getColumnCount() > 0) {
            tblStudents.getColumnModel().getColumn(0).setResizable(false);
            tblStudents.getColumnModel().getColumn(1).setResizable(false);
            tblStudents.getColumnModel().getColumn(2).setResizable(false);
            tblStudents.getColumnModel().getColumn(3).setResizable(false);
            tblStudents.getColumnModel().getColumn(4).setResizable(false);
            tblStudents.getColumnModel().getColumn(5).setResizable(false);
            tblStudents.getColumnModel().getColumn(6).setResizable(false);
            tblStudents.getColumnModel().getColumn(7).setResizable(false);
            tblStudents.getColumnModel().getColumn(8).setResizable(false);
            tblStudents.getColumnModel().getColumn(9).setResizable(false);
            tblStudents.getColumnModel().getColumn(10).setResizable(false);
            tblStudents.getColumnModel().getColumn(11).setResizable(false);
        }

        lblArama.setBackground(new java.awt.Color(255, 255, 255));
        lblArama.setFont(new java.awt.Font("Tahoma", 0, 18)); // NOI18N
        lblArama.setText("Arama:");

        txtArama.setFont(new java.awt.Font("Tahoma", 0, 18)); // NOI18N
        txtArama.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyReleased(java.awt.event.KeyEvent evt) {
                txtAramaKeyReleased(evt);
            }
        });

        lblOgrNo.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N
        lblOgrNo.setText("Öğrenci Numarası:");

        txtOgrNo.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N
        txtOgrNo.setForeground(new java.awt.Color(51, 51, 51));

        lblOgrAd.setBackground(new java.awt.Color(204, 204, 204));
        lblOgrAd.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N
        lblOgrAd.setText("Öğrenci Adı:");

        txtOgrAd.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N

        lblMat.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N
        lblMat.setText("Matematik:");

        txtMat.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N

        lblEdeb.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N
        lblEdeb.setText("Edebiyat:");

        txtEdeb.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N

        lblTar.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N
        lblTar.setText("Tarih:");

        txtTar.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N

        lblCog.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N
        lblCog.setText("Coğrafya:");

        txtCog.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N

        lblDin.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N
        lblDin.setText("Din Kültür:");

        txtDin.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N

        lblFel.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N
        lblFel.setText("Felsefe:");

        txtFel.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N

        lblKim.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N
        lblKim.setText("Kimya:");

        txtKim.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N

        lblFiz.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N
        lblFiz.setText("Fizik:");

        txtFiz.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N

        lblBiyo.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N
        lblBiyo.setText("Biyoloji:");

        btnEkle.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N
        btnEkle.setText("EKLE");
        btnEkle.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnEkleActionPerformed(evt);
            }
        });

        txtBiyo.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N

        txtSil.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N

        btnSil.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        btnSil.setText("Numaralı Öğrenciyi Sil");
        btnSil.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnSilActionPerformed(evt);
            }
        });

        lblMassage.setFont(new java.awt.Font("Tahoma", 0, 18)); // NOI18N

        txtSirala.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N

        btnSirala.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        btnSirala.setText("Göre Sırala");
        btnSirala.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnSiralaActionPerformed(evt);
            }
        });

        lblPuan.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N
        lblPuan.setText("Puan:");

        txtPuan.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 791, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                    .addComponent(txtSirala, javax.swing.GroupLayout.DEFAULT_SIZE, 87, Short.MAX_VALUE)
                                    .addComponent(txtSil))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                    .addComponent(btnSil, javax.swing.GroupLayout.DEFAULT_SIZE, 180, Short.MAX_VALUE)
                                    .addComponent(btnSirala, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
                            .addGroup(layout.createSequentialGroup()
                                .addComponent(lblArama, javax.swing.GroupLayout.PREFERRED_SIZE, 71, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(txtArama, javax.swing.GroupLayout.PREFERRED_SIZE, 309, javax.swing.GroupLayout.PREFERRED_SIZE)))
                        .addContainerGap(209, Short.MAX_VALUE))
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                            .addComponent(lblMassage, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                                    .addComponent(lblOgrAd, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                    .addComponent(lblOgrNo, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                    .addComponent(txtOgrNo)
                                    .addComponent(txtOgrAd, javax.swing.GroupLayout.DEFAULT_SIZE, 100, Short.MAX_VALUE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                    .addComponent(lblMat, javax.swing.GroupLayout.DEFAULT_SIZE, 68, Short.MAX_VALUE)
                                    .addComponent(lblEdeb, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                    .addComponent(txtMat)
                                    .addComponent(txtEdeb, javax.swing.GroupLayout.DEFAULT_SIZE, 100, Short.MAX_VALUE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                    .addComponent(lblTar, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                    .addComponent(lblCog, javax.swing.GroupLayout.DEFAULT_SIZE, 68, Short.MAX_VALUE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                    .addComponent(txtTar)
                                    .addComponent(txtCog, javax.swing.GroupLayout.DEFAULT_SIZE, 100, Short.MAX_VALUE))))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addComponent(lblDin, javax.swing.GroupLayout.DEFAULT_SIZE, 68, Short.MAX_VALUE)
                            .addComponent(lblFel, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addComponent(txtDin)
                            .addComponent(txtFel, javax.swing.GroupLayout.DEFAULT_SIZE, 100, Short.MAX_VALUE))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addComponent(lblKim, javax.swing.GroupLayout.DEFAULT_SIZE, 68, Short.MAX_VALUE)
                            .addComponent(lblFiz, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addComponent(txtKim)
                            .addComponent(txtFiz, javax.swing.GroupLayout.DEFAULT_SIZE, 100, Short.MAX_VALUE))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addGroup(layout.createSequentialGroup()
                                .addComponent(lblBiyo, javax.swing.GroupLayout.PREFERRED_SIZE, 68, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(txtBiyo, javax.swing.GroupLayout.PREFERRED_SIZE, 100, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addGroup(layout.createSequentialGroup()
                                .addComponent(lblPuan, javax.swing.GroupLayout.PREFERRED_SIZE, 68, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(txtPuan))
                            .addComponent(btnEkle, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                        .addGap(0, 0, Short.MAX_VALUE))))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(11, 11, 11)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(lblArama)
                    .addComponent(txtArama, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 337, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(45, 45, 45)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(txtSil, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(btnSil))
                        .addGap(51, 51, 51)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(txtSirala, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(btnSirala))))
                .addGap(31, 31, 31)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(lblOgrNo, javax.swing.GroupLayout.PREFERRED_SIZE, 21, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(txtOgrNo, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(lblMat)
                    .addComponent(txtMat, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(lblTar)
                    .addComponent(txtTar, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(lblDin)
                    .addComponent(txtDin, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(lblKim)
                    .addComponent(txtKim, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(lblBiyo)
                    .addComponent(txtBiyo, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(lblOgrAd, javax.swing.GroupLayout.PREFERRED_SIZE, 21, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(txtOgrAd, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(lblEdeb)
                    .addComponent(txtEdeb, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(lblCog)
                    .addComponent(txtCog, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(lblFel)
                    .addComponent(txtFel, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(lblFiz)
                    .addComponent(txtFiz, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(lblPuan)
                    .addComponent(txtPuan, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(btnEkle)
                .addGap(10, 10, 10)
                .addComponent(lblMassage)
                .addContainerGap(82, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void txtAramaKeyReleased(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_txtAramaKeyReleased
       String searchKey= txtArama.getText();
        TableRowSorter<DefaultTableModel> tableRowSorter = new TableRowSorter<DefaultTableModel>(model);
        tblStudents.setRowSorter(tableRowSorter);
        tableRowSorter.setRowFilter(RowFilter.regexFilter(searchKey));
    }//GEN-LAST:event_txtAramaKeyReleased

    private void btnEkleActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnEkleActionPerformed
        Connection  connection = null;
        DbHelper dbHelper = new DbHelper();
        PreparedStatement statement = null;
        try{
            connection = dbHelper.getConnection();
            String sql = "INSERT INTO `students`.`students` (`ogr_no`, `ogr_ad`, `mat`, `edeb`, `tar`, `cog`, `din`, `fel`, `kim`, `fiz`, `biyo`, `puan`) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);";
            statement = connection.prepareStatement(sql);
            statement.setInt(1,Integer.valueOf(txtOgrNo.getText()));
            statement.setString(2,txtOgrAd.getText());
            statement.setDouble(3,Double.valueOf(txtMat.getText()));
            statement.setDouble(4,Double.valueOf(txtEdeb.getText()));
            statement.setDouble(5,Double.valueOf(txtTar.getText()));
            statement.setDouble(6,Double.valueOf(txtCog.getText()));
            statement.setDouble(7,Double.valueOf(txtDin.getText()));
            statement.setDouble(8,Double.valueOf(txtFel.getText()));
            statement.setDouble(9,Double.valueOf(txtKim.getText()));
            statement.setDouble(10,Double.valueOf(txtFiz.getText()));
            statement.setDouble(11,Double.valueOf(txtBiyo.getText()));
            statement.setDouble(12,Double.valueOf(txtPuan.getText()));
            int result = statement.executeUpdate();
            polulateTable();
            lblMassage.setText("");
            txtOgrNo.setText("");
            txtOgrAd.setText("");
            txtMat.setText("");
            txtEdeb.setText("");
            txtTar.setText("");
            txtCog.setText("");
            txtDin.setText("");
            txtFel.setText("");
            txtKim.setText("");
            txtFiz.setText("");
            txtBiyo.setText("");
            txtPuan.setText("");
        }catch(SQLException e){
            dbHelper.showErrorMassage(e);
            lblMassage.setText("Aynı Numarada İki Kişi Olmaz");
        }
    }//GEN-LAST:event_btnEkleActionPerformed

    private void btnSilActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnSilActionPerformed
        Connection  connection = null;
        DbHelper dbHelper = new DbHelper();
        PreparedStatement statement = null;
        try{
             connection = dbHelper.getConnection();
            String sql = "DELETE FROM `students`.`students` WHERE ogr_no = ? ;";
            statement = connection.prepareStatement(sql);
            statement.setInt(1,Integer.valueOf(txtSil.getText()));
            int result = statement.executeUpdate();
            polulateTable();
            txtSil.setText("");
        }catch(SQLException e){
            dbHelper.showErrorMassage(e);
        }finally {
            try {
                statement.close();
                connection.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }

        }
    }//GEN-LAST:event_btnSilActionPerformed

    private void btnSiralaActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnSiralaActionPerformed
        model = (DefaultTableModel)tblStudents.getModel();
        model.setRowCount(0);
        try{
            ArrayList<Students> students = sirala();

            for (Students students1 : students){
                Object[] row = {
                        students1.getOgrenciNo(),
                        students1.getOgrenciAdi(),
                        students1.getMatematik(),
                        students1.getEdebiyat(),
                        students1.getTarih(),
                        students1.getCografya(),
                        students1.getDin(),
                        students1.getFelsefe(),
                        students1.getKimya(),
                        students1.getFizik(),
                        students1.getBiyoloji(),
                        students1.getPuan()};
                model.addRow(row);
            }
            txtSirala.setText("");
        }catch (SQLException e){

        }
    }//GEN-LAST:event_btnSiralaActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(demo.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(demo.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(demo.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(demo.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new demo().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnEkle;
    private javax.swing.JButton btnSil;
    private javax.swing.JButton btnSirala;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JLabel lblArama;
    private javax.swing.JLabel lblBiyo;
    private javax.swing.JLabel lblCog;
    private javax.swing.JLabel lblDin;
    private javax.swing.JLabel lblEdeb;
    private javax.swing.JLabel lblFel;
    private javax.swing.JLabel lblFiz;
    private javax.swing.JLabel lblKim;
    private javax.swing.JLabel lblMassage;
    private javax.swing.JLabel lblMat;
    private javax.swing.JLabel lblOgrAd;
    private javax.swing.JLabel lblOgrNo;
    private javax.swing.JLabel lblPuan;
    private javax.swing.JLabel lblTar;
    private javax.swing.JTable tblStudents;
    private javax.swing.JTextField txtArama;
    private javax.swing.JTextField txtBiyo;
    private javax.swing.JTextField txtCog;
    private javax.swing.JTextField txtDin;
    private javax.swing.JTextField txtEdeb;
    private javax.swing.JTextField txtFel;
    private javax.swing.JTextField txtFiz;
    private javax.swing.JTextField txtKim;
    private javax.swing.JTextField txtMat;
    private javax.swing.JTextField txtOgrAd;
    private javax.swing.JTextField txtOgrNo;
    private javax.swing.JTextField txtPuan;
    private javax.swing.JTextField txtSil;
    private javax.swing.JTextField txtSirala;
    private javax.swing.JTextField txtTar;
    // End of variables declaration//GEN-END:variables
}
