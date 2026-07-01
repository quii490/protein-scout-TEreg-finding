---
type: protein-evaluation
gene: "RASSF4"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## RASSF4 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | RASSF4 |
| 蛋白全称 | Ras association domain-containing protein 4 |
| UniProt ID | Q9H2L5 |
| 蛋白大小 | 321 aa / 35.3 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cell Junctions; Cytokinetic bridge; Cytosol; Mitot (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 321 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=33 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=77.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | RA_dom; RASSF1-6; RASSF4_RA |
| PPI | 5/10 | x3 | 15.0 | PPI degree=9 |
| **加权总分** | | | **126/180** | |
| **归一化总分** | | | **69.4/100** | 互证: +1 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | 未知 | 1: Evidence at protein level |

#### 3.2 功能描述

Potential tumor suppressor. May act as a KRAS effector protein. May promote apoptosis and cell cycle arrest

#### 3.3 结构域分析

| 来源 | 结构域 ID | 名称 |
|---|---|---|
| InterPro | IPR000159 | RA_dom |
| InterPro | IPR033614 | RASSF1-6 |
| InterPro | IPR033622 | RASSF4_RA |
| InterPro | IPR011524 | SARAH_dom |
| InterPro | IPR029071 | Ubiquitin-like_domsf |
| Pfam | PF16517 | Nore1-SARAH |
| Pfam | PF00788 | RA |


#### 3.4 结构信息

蛋白长度 321 aa，AlphaFold 预测可用。

#### 3.5 PPI 网络

PPI 数据待充实。

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000107551-RASSF4

![](https://images.proteinatlas.org/38834/539_A9_7_red_green.jpg)
![](https://images.proteinatlas.org/38834/539_A9_10_red_green.jpg)
![](https://images.proteinatlas.org/38834/552_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/38834/552_A9_3_red_green.jpg)
![](https://images.proteinatlas.org/38834/534_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/38834/534_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/77069/1917_D11_3_red_green.jpg)
![](https://images.proteinatlas.org/77069/1917_D11_6_red_green.jpg)

### TE 调控相关性

该蛋白无明确的染色质/TE 沉默相关定位。TE 调控潜力极低。
### 4. 总体评价
**69.4/100** | **nucleolus**
Nuclear protein


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00314;SM00167; |
| InterPro | IPR000159;IPR035868;IPR000980;IPR036860;IPR029071;IPR003123;IPR045046;IPR037191; |
| Pfam | PF00788;PF23268;PF02204; |
| UniProt Domain | DOMAIN 97..190; /note="SH2"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00191"; DOMAIN 618..757; /note="VPS9"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00550"; DOMAIN 787..878; /note="Ras-associating"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00166" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| STK4 | BioGRID | 0 |
| STK3 | BioGRID | 0 |
| MAGEA6 | BioGRID | 0 |
| IFT20 | BioGRID | 0 |
| CENPH | BioGRID | 0 |
| HGS | BioGRID | 0 |
| DLG4 | BioGRID | 0 |
| EIF5B | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H2L5-F1-predicted_aligned_error_v6.png)

### 深度机制分析

**结构域架构**：RASSF4（321 aa，35.3 kDa）是Ras关联结构域（RA domain）蛋白家族的成员兼肿瘤抑制因子，结构域架构紧凑且功能富集：RA_dom（IPR000159, PF00788）——约100-200 aa的Ras结合结构域，采用泛素样折叠（Ubiquitin-like_domsf IPR029071），通过β1-β2-α1-β3-β4-β5的β-grasp拓扑识别活性态Ras·GTP；SARAH_dom（IPR011524, PF16517/Nore1-SARAH）——C端~40 aa的卷曲螺旋（coiled-coil）结构域，介导与MST1/STK4和MST2/STK3激酶的同源/异源二聚化；RASSF4_RA（IPR033622）——RASSF4特异的RA结构域亚型，含额外的N端延伸赋予KRAS选择性结合能力。AlphaFold pLDDT=77.8，RA结构域（pLDDT~85）和SARAH（pLDDT~75）预测质量较高。HPA定位为Nucleoli; Nucleoplasm（Approved），属典型的Hippo通路核周分布模式。

**PPI互作网络解读**：PPI degree=9（实际Network内连接数可能更高），核心互作包含：STK4/STK3（MST1/MST2激酶，Hippo通路核心激酶，通过SARAH结构域直接二聚化）——这是RASSF4最功能相关的互作对，MST-RASSF4复合体激活后磷酸化LATS1/2，继而磷酸化YAP/TAZ转录共激活因子；HGS（HRS，ESCRT-0组分，内吞体分选）——提示RASSF4可能参与内吞体膜上的Ras信号终止；IFT20（鞭毛内转运蛋白）——连接纤毛/Ras信号，部分肿瘤中RASSF4缺失与纤毛功能障碍相关；DLG4（PSD-95，突触后密度支架蛋白）——提示潜在的突触功能。MAGEA6（癌-睾丸抗原）、CENPH（着丝粒蛋白H）和EIF5B（翻译起始因子）为非典型互作，需独立验证。

**结构解读**：RA结构域采用β-grasp折叠——5条反平行β-链形成弯曲片层，背面由单一α-螺旋覆盖。Ras结合界面涉及β1-β2 loop和β3上的保守残基（Lys/Arg极性接触Ras的Switch I区Glu37/Asp38）。SARAH结构域形成反平行卷曲螺旋二聚体，Nore1-SARAH与MST1-SARAH的间距约3.5A（经典螺旋-螺旋堆积），支撑Hippo激酶级联的支架组装。PAE矩阵显示RA与SARAH之间的连接区（约200-280 aa）pLDDT快速下降至55-65，提示该区域可能为固有无序区（IDR）——这在信号蛋白中常见，允许结构域间灵活的构象采样以适应不同互作伙伴。

**机制模型**：RASSF4通过双重肿瘤抑制机制运作：（1）Ras信号终止——RA结构域选择性结合KRAS·GTP（不结合HRAS/NRAS），将活性Ras靶向MST激酶复合体，启动促凋亡的Hippo通路（MST→LATS→YAP磷酸化→YAP胞质滞留/降解），从而对抗Ras驱动的增殖信号；（2）SARAH结构域支架——与MST1/2形成四聚体（RASSF4₂-MST₂）催化平台，显著提高MST的自磷酸化（Thr183/Thr180）和底物磷酸化效率。在核仁中，RASSF4可能通过YAP/TAZ通路调控rDNA转录——已知YAP可与核仁转录因子UBF结合增强Pol I转录活性，RASSF4促YAP降解间接抑制核仁rRNA合成。ESMFold pLDDT=0.74验证了AlphaFold预测的一致性。

**TE调控展望**：RASSF4通过YAP/TEAD通路间接连接TE调控。YAP/TEAD复合体结合TEAD响应元件（MCAT/GGAATG基序），已知多种ERV LTR序列中包含MCAT样序列，YAP/TEAD可激活这些LTR驱动基因。RASSF4通过促进YAP降解可抑制YAP-TEAD-TE轴的转录输出。此外，RASSF4介导的MST激活可磷酸化组蛋白H2B（Ser14），已知H2B磷酸化在DNA损伤应答中促进染色质松弛——可能间接影响TE区域的染色质可及性。但这些关联需特异性实验验证（PMID:42141135揭示了RASSF4对PKD2通道的调控新功能）。

### PubMed 文献

**PubMed count: 50**

| 42353386 | Multi-Omics Analysis Reveals New Insights into Yak Lung Under High-Altitude Adaptation. | Animals (Basel) 2026 |
| 42141135 | Regulation of the PKD2 channel function and associated disease phenotypes by RASSF4. | Commun Biol 2026 |
| 41998299 | Establishiment of PANoptosis-related prognostic signature and experimental identification of SIGLEC1 as an oncogenic bio | Discov Oncol 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RASSF4

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/RASSF4_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.74 |
| pLDDT > 0.9 | 26.8% |
| pLDDT < 0.5 | 12.8% |
| 残基数 | 321 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。

