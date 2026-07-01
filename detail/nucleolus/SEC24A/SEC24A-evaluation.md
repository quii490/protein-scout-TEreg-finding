---
type: protein-evaluation
gene: "SEC24A"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SEC24A 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | SEC24A |
| 蛋白全称 | Protein transport protein Sec24A |
| UniProt ID | O95486 |
| 蛋白大小 | 1093 aa / 120.2 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoli fibrillar center; Vesicles (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 1093 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=38 |
| 三维结构 | 9/10 | x3 | 27.0 | pLDDT=75.5; PDB=16 |
| 调控结构域 | 4/10 | x2 | 8.0 | ADF-H/Gelsolin-like_dom_sf; Beta-sandwich_Sec23_24; Gelsolin-like_dom |
| PPI | 8/10 | x3 | 24.0 | PPI degree=238 |
| **加权总分** | | | **142/180** | |
| **归一化总分** | | | **78.7/100** | 互证: +2 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | 未知 | 1: Evidence at protein level |

#### 3.2 功能描述

Component of the coat protein complex II (COPII) which promotes the formation of transport vesicles from the endoplasmic reticulum (ER). The coat has two main functions, the physical deformation of the endoplasmic reticulum membrane into vesicles and the selection of cargo molecules for their transp

#### 3.3 结构域分析

| 来源 | 结构域 ID | 名称 |
|---|---|---|
| InterPro | IPR029006 | ADF-H/Gelsolin-like_dom_sf |
| InterPro | IPR012990 | Beta-sandwich_Sec23_24 |
| InterPro | IPR007123 | Gelsolin-like_dom |
| InterPro | IPR036180 | Gelsolin-like_dom_sf |
| InterPro | IPR006900 | Sec23/24_helical_dom |
| InterPro | IPR036175 | Sec23/24_helical_dom_sf |
| InterPro | IPR006896 | Sec23/24_trunk_dom |
| InterPro | IPR050550 | SEC23_SEC24_subfamily |


#### 3.4 结构信息

蛋白长度 1093 aa，AlphaFold 预测可用。

#### 3.5 PPI 网络

PPI 数据待充实。

### TE 调控相关性

该蛋白无明确的染色质/TE 沉默相关定位。TE 调控潜力极低。
### 4. 总体评价
**78.7/100** | **nucleolus**
Nuclear protein


### 深度机制分析

SEC24A是COPII被膜复合体的核心货物分选亚基，其多结构域架构精确对应了囊泡出芽过程的分子分工。N端Sec23/24 trunk结构域(IPR006896)和Sec23/24 helical结构域(IPR006900)协同介导与SEC23A的异源二聚化——后者是其直接结合伙伴(BioGRID)，二者共同构成COPII内壳层的骨架。C端的gelsolin样结构域(IPR007123, IPR036180)和ADF-H/gelsolin样超家族折叠(IPR029006)构成货物识别界面，通过识别跨膜货物胞质尾部的内质网出口信号肽基序(di-acidic、di-hydrophobic等)实现选择性货物分选。pLDDT为75.5表明该蛋白存在显著的内在无序区域，这与SEC24作为大型支架蛋白(1093 aa, 120.2 kDa)的特征一致——柔性环区和连接片段允许构象适应以识别数十种不同货物。PDB收录16个实验结构进一步确证了其多结构域折叠的可靠性，尤其Sec23/24异源二聚体界面已在晶体学层面被充分解析。

PPI网络揭示了SEC24A功能的多维度调控层次。其与CUL3(BioGRID)的互作尤为值得关注——CUL3是Cullin-RING E3泛素连接酶复合体的支架蛋白，提示SEC24A的稳定性或COPII组装效率可能受泛素-蛋白酶体系统调控。TRIP13(BioGRID)作为AAA+ ATP酶参与有丝分裂检查点和减数分裂重组，这一连接暗示SEC24A可能存在细胞周期依赖性的分泌调控——分裂期ER出口效率的变化对于细胞器遗传至关重要。同家族SEC24B、SEC24C、SEC24D的同时出现(BioGRID)提示COPII内壳层可能存在SEC24异源多聚体，不同旁系同源物的货物选择性差异可通过组合扩展识别谱。AHCYL1(IRBIT, BioGRID)作为IP3受体的竞争性调控蛋白，其互作暗示内质网钙信号可能间接调控COPII囊泡出芽——钙离子通过IP3受体释放后，AHCYL1从IP3受体解离并可能影响SEC24A的构象或定位。

SEC24A在核仁纤维中心(Nucleoli fibrillar center)的定位与经典COPII蛋白的内质网出口位点(ERES)定位存在显著差异，这一反常定位存在多种可能的机制解释：(1)核仁定位可能是SEC24A参与核仁-细胞质大分子运输的非经典功能的体现——核仁是核糖体生物发生的场所，而COPII蛋白可能参与将核糖体前体或核仁蛋白转运至ER；(2)文献中SEC24A通过调控PCSK9分泌影响血浆胆固醇水平(PMID:42339786)的功能连接提示，核仁定位可能与SREBP胆固醇代谢转录程序的调控有关，核仁是多个代谢转录因子的锚定位点；(3)NHA2钠/质子反向转运蛋白的运输依赖cornichon COPII货物受体和SEC24A(PMID:41676957)，进一步验证了SEC24A在特定货物识别中的不可替代性。ING5/OIP5-AS1/miR-381-3p/SEC24A轴(PMID:41378010)揭示的肺癌调控通路中，SEC24A作为ceRNA网络的下游效应器，其表达水平受竞争性内源RNA机制精细调控，这为其在肿瘤中的差异表达提供了上游机制。

综合分子机制模型：SEC24A通过Sec23/24 trunk和helical结构域与SEC23A形成稳定异源二聚体并组装入COPII内壳层，gelsolin样货物识别域以构象适应方式捕获货物蛋白的ER出口信号，CUL3和TRIP13分别通过泛素化和细胞周期依赖性输入调控COPII组装动态，AHCYL1提供钙信号对分泌的间接调控。其核仁定位及PCSK9/NHA2通路的功能关联提示SEC24A在核-细胞质界面的非经典功能值得深度挖掘。在转化研究方面，SEC24A-PCSK9分泌通路使其成为高胆固醇血症的间接治疗靶点——靶向SEC24A的特定货物识别界面可能选择性抑制PCSK9分泌而不影响整体COPII功能，而ING5/OIP5-AS1/miR-381-3p/SEC24A轴的鉴定则为肺癌提供了表观遗传-转录后调控层面的干预靶标。


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR029006;IPR012990;IPR007123;IPR036180;IPR006900;IPR036175;IPR006896;IPR050550;IPR041742;IPR036465;IPR006895; |
| Pfam | PF00626;PF08033;PF04815;PF04811;PF04810; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TRIP13 | BioGRID | 0 |
| CUL3 | BioGRID | 0 |
| SEC23A | BioGRID | 0 |
| SEC24C | BioGRID | 0 |
| SEC24D | BioGRID | 0 |
| SEC24B | BioGRID | 0 |
| AHCYL1 | BioGRID | 0 |
| CLNS1A | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O95486-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 57**

| 42339786 | Correction: SEC24A deficiency lowers plasma cholesterol through reduced PCSK9 secretion. | Elife 2026 |
| 41676957 | Trafficking of the human Na(+)/H(+) antiporter NHA2 to the plasma membrane requires cornichon COPII cargo receptors. | Protein Sci 2026 |
| 41378010 | ING5-mediated regulation of lung cancer progression via the OIP5-AS1/miR-381-3p/SEC24A axis. | Transl Cancer Res 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SEC24A

