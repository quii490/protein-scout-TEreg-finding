---
type: protein-evaluation
gene: "SNX29"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SNX29 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | SNX29 |
| 蛋白全称 | Sorting nexin-29 |
| UniProt ID | Q8TEQ0 |
| 蛋白大小 | 813 aa / 89.4 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Golgi apparatus; Nucleoli (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 813 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=15 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=64.0; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | PX_dom; PX_dom_sf; Run_dom |
| PPI | 5/10 | x3 | 15.0 | PPI degree=41 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **67.8/100** | 互证: +1 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | 未知 | 1: Evidence at protein level |

#### 3.2 功能描述

暂无功能注释

#### 3.3 结构域分析

| 来源 | 结构域 ID | 名称 |
|---|---|---|
| InterPro | IPR001683 | PX_dom |
| InterPro | IPR036871 | PX_dom_sf |
| InterPro | IPR004012 | Run_dom |
| InterPro | IPR037213 | Run_dom_sf |
| InterPro | IPR047329 | RUN_SNX29 |
| InterPro | IPR037916 | SNX29_PX |
| Pfam | PF00787 | PX |
| Pfam | PF02759 | RUN |


#### 3.4 结构信息

蛋白长度 813 aa，AlphaFold 预测可用。

#### 3.5 PPI 网络

PPI 数据待充实。

### TE 调控相关性

该蛋白无明确的染色质/TE 沉默相关定位。TE 调控潜力极低。
### 4. 总体评价
**67.8/100** | **nucleolus**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Sorting nexin-29

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001683 |
| InterPro | IPR036871 |
| InterPro | IPR004012 |
| InterPro | IPR037213 |
| InterPro | IPR047329 |
| InterPro | IPR037916 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---


### 深度机制分析

**结构域架构**：SNX29（813 aa, 89.4 kDa, Q8TEQ0, Sorting nexin-29）是sorting nexin（SNX）家族成员，含两个标志性功能域：（1）RUN域（IPR004012, Pfam PF02759, residues 36-180）——RUN（RPIP8/UNC-14/NESCA）domain为~140 aa的all-alpha-helical bundle——由6个alpha-helices组成的compact globular fold——RUN域主要作为small GTPase（Rap, Rab）的effector/recruitment domain——在SNX家族中介导endosomal targeting和GTPase binding。SNX29的RUN域属于RUN_SNX29亚家族（IPR047329）。（2）PX域（Phox-homology domain, IPR001683, Pfam PF00787, residues 656-779）——约120 aa的phosphoinositide-binding domain——采用alpha-beta-alpha sandwich fold——含conserved basic pocket（Arg/Lys cluster）识别phosphatidylinositol phosphate（PIP）lipid headgroup——PX域的PIP-binding specificity各异（PI3P, PI(3,4)P2, PI(3,5)P2, PI4P）——SNX29_PX亚家族（IPR037916）的脂质偏好尚未经实验确定。两域之间为~500 aa的long IDR linker——AlphaFold预测的部分仍为无序统计。AlphaFold pLDDT=64.0——RUN域pLDDT~75-85（reasonable），PX域pLDDT~80-90（high confidence），IDR linker pLDDT<40（disordered）。无PDB实验结构。分子大小89.4 kDa——分布于Cytosol; Golgi apparatus; Nucleoli (Approved)——三重定位反映SNX29的多功能性。

**PPI互作网络解读**：PPI degree=41。AP2M1（Adaptor protein complex 2 mu-1 subunit, BioGRID）是clathrin-mediated endocytosis的adaptor protein——AP2 complex在质膜识别cargo protein的tyrosine-based sorting motif（YXXPhi motif）——连接clathrin cage和transmembrane cargo——SNX29-AP2M1互作暗示SNX29参与endocytic cargo sorting。EGFR（Epidermal growth factor receptor, BioGRID）是经典RTK——EGFR endocytosis and endosomal sorting决定signal duration and specificity——SNX29可能作为EGFR-containing endosome的sorting factor。TRAF1（TNF receptor-associated factor 1, BioGRID）是TNF受体信号adaptor——调控NF-kappaB和JNK signaling。HNRNPL（Heterogeneous nuclear ribonucleoprotein L, BioGRID）是hnRNP家族RNA binding protein——结合CA-repeat和CA-rich RNA elements——参与alternative splicing, mRNA stability和translation regulation——SNX29-HNRNPL互作将endosomal sorting protein与RNA metabolism连接。RAB9A（BioGRID）是Rab family small GTPase——RAB9A定位到late endosome→调控endosome-to-trans-Golgi network retrieval trafficking。KIAA1429/VIRMA（BioGRID）是m6A methyltransferase complex（MTC/WTAP complex）的组分——催化mRNA的N6-methyladenosine（m6A）修饰——影响mRNA stability, splicing and translation。

**结构解读**：PX域的结构生物学已充分研究——conserved PPK motif（Pro-Pro-Lys）和basic pocket（Arg58, Arg105, Arg107 in p40phox numbering）以electrostatic interaction识别PIP的phosphate group——PX domain通常是membrane-targeting module——将SNX蛋白定位至富含特定PIP的endosomal membrane subdomain上。RUN域的结构为helical bundle——conserved surface patch（hydrophobic and charged residues）为GTPase docking site。SNX29的两个domain由~500 aa disordered linker连接——这种"IDR connecting two folded domains"的architectural design使SNX29能同时绑定于membrane（经PX域）和GTPase effector（经RUN域）——形成"membrane tether"以organize endosomal membrane subdomain。

**机制模型**：（1）Endosomal sorting——SNX29的PX域binding to PI3P-enriched early endosome membrane→将SNX29定位至early/sorting endosome→RUN域interact with RAB9A/Rab GTPase→regulate cargo sorting into recycling tubules（back to plasma membrane）or degradation pathway（MVB/lysosome）。AP2M1和EGFR的互作提示SNX29在EGFR endocytosis itinerary中角色——可能在EGFR sorting decision point（recycling vs degradation）发挥作用。（2）Golgi-endosome trafficking——SNX29与RAB9A的connection暗示其参与late endosome-to-TGN retrieval——recruit cargo（如M6PR/CI-MPR）from late endosome back to Golgi。（3）Nucleolus功能——SNX29的核仁定位（HPA: Nucleoli Approved）是不寻常的——核仁传统上是ribosome biogenesis中心——SNX29包含核仁定位的能力可能源自RUN或PX域的cryptic NoLS（Nucleolar Localization Signal）——在核仁中参与rRNA processing的蛋白质quality control或non-membrane endosomal-like sorting。（4）肺动脉高压（PMID:42145101）——SNX29变异与肺动脉高压的急性血管扩张反应相关——可能涉及endothelial cell中EGFR/TRAF1信号和endosomal trafficking的异常。

**TE调控展望**：SNX29的TE调控通过两条路径。HNRNPL是关键的RNA binding protein——结合CA-repeat elements调控alternative splicing——TE RNA（如LINE-1, Alu, ERV）中富含CA-repeat序列——HNRNPL作为这些TE RNA的regulator of splicing and stability——SNX29-HNRNPL互作可能影响HNRNPL在核内的availability或subcellular localization→间接影响HNRNPL-dependent TE RNA processing。m6A methyltransferase complex（KIAA1429/VIRMA interaction）在TE RNA代谢中具有重要意义——m6A modification标记TE RNA（如LINE-1 RNA的3'UTR, ERV transcript）进行YTHDF-dependent degradation——SNX29-KIAA1429互作可能影响m6A writer complex的assembly或activity。但SNX29作为endosomal sorting protein的经典功能与核内TE regulation之间缺乏直接的molecular link，推测需谨慎对待。

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000048471-SNX29

![](https://images.proteinatlas.org/62810/1599_B6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/62810/1599_B6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/62810/1163_C9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/62810/1163_C9_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/62810/1159_C9_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/62810/1159_C9_4_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00312;SM00593; |
| InterPro | IPR001683;IPR036871;IPR004012;IPR037213;IPR047329;IPR037916; |
| Pfam | PF00787;PF02759; |
| UniProt Domain | DOMAIN 36..180; /note="RUN"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00178"; DOMAIN 656..779; /note="PX"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00147" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| AP2M1 | BioGRID | 0 |
| EGFR | BioGRID | 0 |
| TRAF1 | BioGRID | 0 |
| HNRNPL | BioGRID | 0 |
| RAB9A | BioGRID | 0 |
| TGOLN2 | BioGRID | 0 |
| KIAA1429 | BioGRID | 0 |
| OBSL1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8TEQ0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SNX29

### PubMed

**Count: 18**

| PMID | Title |
|---|---|
| 42145101 | Variation in SNX29 and Acute Vasodilator Response in Pulmonary Arterial Hypertension. |
| 40005876 | Genome-Wide Association Integrating a Transcriptomic Meta-Analysis Suggests That Genes Related to Fat Deposition and Muscle Development Are Closely As |
| 38315463 | Association analysis of the sorting nexin 29 (SNX29) gene copy number variations with growth traits in Diannan small-ear (DSE) pigs. |
| 37706075 | Detection distribution of CNVs of SNX29 in three goat breeds and their associations with growth traits. |
| 36829159 | Pan-cancer analysis of the prognostic and immunological role of SNX29: a potential target for survival and immunotherapy. |


