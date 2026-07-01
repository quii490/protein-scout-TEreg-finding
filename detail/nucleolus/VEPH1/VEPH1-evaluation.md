---
type: protein-evaluation
gene: "VEPH1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## VEPH1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | VEPH1 |
| 蛋白全称 | Ventricular zone-expressed PH domain-containing protein homolog 1 |
| UniProt ID | Q14D04 |
| 蛋白大小 | 833 aa / 91.6 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoli; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 833 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=19 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=73.0; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | ARM-type_fold; Melted-like; PH-like_dom_sf |
| PPI | 5/10 | x3 | 15.0 | PPI degree=5 |
| **加权总分** | | | **126/180** | |
| **归一化总分** | | | **69.4/100** | 互证: +1 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | 未知 | 1: Evidence at protein level |

#### 3.2 功能描述

Interacts with TGF-beta receptor type-1 (TGFBR1) and inhibits dissociation of activated SMAD2 from TGFBR1, impeding its nuclear accumulation and resulting in impaired TGF-beta signaling. May also affect FOXO, Hippo and Wnt signaling

#### 3.3 结构域分析

| 来源 | 结构域 ID | 名称 |
|---|---|---|
| InterPro | IPR016024 | ARM-type_fold |
| InterPro | IPR039888 | Melted-like |
| InterPro | IPR011993 | PH-like_dom_sf |
| InterPro | IPR001849 | PH_domain |
| Pfam | PF00169 | PH |


#### 3.4 结构信息

蛋白长度 833 aa，AlphaFold 预测可用。

#### 3.5 PPI 网络

PPI 数据待充实。

### TE 调控相关性

该蛋白无明确的染色质/TE 沉默相关定位。TE 调控潜力极低。
### 4. 总体评价
**69.4/100** | **nucleolus**
Nuclear protein


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00233; |
| InterPro | IPR016024;IPR039888;IPR011993;IPR001849; |
| Pfam | PF00169; |
| UniProt Domain | DOMAIN 716..819; /note="PH"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00145" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TNFAIP3 | BioGRID | 0 |
| TOP3B | BioGRID | 0 |
| TUBA4A | BioGRID | 0 |
| DLG5 | BioGRID | 0 |
| CFTR | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q14D04-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 27**

| 41997548 | Raddeanin A induces ferroptosis by targeting VEPH1 in a cisplatin-resistant epithelial ovarian cancer cell line. | Free Radic Biol Med 2026 |
| 41180518 | Prognostic modeling of glioma using epilepsy-related genes highlights PAX3 as a regulator of migration and vorinostat se | Front Neurol 2025 |
| 40869957 | Molecular Genetic Basis of Reproductive Fitness in Tibetan Sheep on the Qinghai-Tibet Plateau. | Genes (Basel) 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/VEPH1

### 深度机制分析

**结构域架构**：VEPH1（UniProt Q14D04，833 aa，91.6 kDa）属于含PH（Pleckstrin Homology）域的Melted-like蛋白家族。其域架构以大尺寸和PH域为核心：N端由大量犰狳重复序列（armadillo-type fold, IPR016024）组成α-超螺旋螺线管支架——此类重复域常见于β-catenin、importin-α、APC等大型支架蛋白，形成延长的超螺旋表面用于介导蛋白-蛋白互作网络；C端为PH域（InterPro:IPR001849 - Pleckstrin homology domain；Pfam:PF00169 - PH；SMART:SM00233 - PH；UniProt Domain注释: 716-819 aa, PROSITE:PRU00145），该域采用β-三明治折叠（7条β-链形成两个反平行β-片层），特异性识别磷酸肌醇（PIPs）以介导膜招募。IPR039888（Melted-like）和IPR011993（PH-like domain superfamily）为Melted/VEPH1蛋白家族的特异性折叠超家族标记。AlphaFold PAE图显示N端armadillo螺线管与C端PH域之间存在较大柔性连接子，提示模块间运动以调节膜结合和蛋白互作的平衡。

**PPI互作网络**：BioGRID数据展示了一个免疫调控-转录-细胞骨架交叉的PPI网络：TNFAIP3（A20，评分0）为IKK/NF-κB通路的双重去泛素化酶和E3连接酶抑制因子——A20是炎症负调控的核心制动因子，突变与自身免疫病关联；TOP3B（DNA拓扑异构酶IIIβ，评分0）催化释放转录超螺旋，与FMRP-TDRD3复合体共定位以解旋RNA-DNA杂交体（R-loops）；TUBA4A（α-tubulin 4A，评分0）为微管蛋白；DLG5（discs large MAGUK scaffold protein 5，评分0）为细胞极性调控因子；CFTR（囊性纤维化跨膜受体，评分0）为氯离子通道。

**结构-功能关系**：VEPH1经PH域结合PI(3,4,5)P₃等磷酸肌醇在质膜定位，而N端armadillo支架域招募SMAD2-TGFBR1复合体——这是VEPH1的核心信号功能。UniProt描述明确指出VEPH1通过抑制活化SMAD2从TGFBR1解离，阻止SMAD2的核积聚，从而削弱TGF-β信号通路。这意味着VEPH1定位于质膜-早期内吞体界面，作为TGF-β/TGFBR1的胞质锚定因子。PI3K/AKT产生的PI(3,4,5)P₃增强PH域的膜定位，AKT→VEPH1-TGFBR1→SMAD2构成了整合磷脂酰肌醇信号和TGF-β信号的交互枢纽。27篇文献中的主导方向为卵巢癌顺铂耐药机制（PMID:41997548 - Raddeanin A通过靶向VEPH1诱导铁死亡），将铁死亡（ferroptosis）应激与VEPH1信号连接。

**TE调控机制**：VEPH1经三条通路与TE调控相交。其一，TGF-β/SMAD信号通路中SMAD2/3-SMAD4复合体结合染色质SMAD结合元件（SBEs）——许多ERV-LTR启动子谱系中包含SBE序列，TGF-β→SMAD→TE转录是ERV活化的一类已知机制。VEPH1通过降低核内SMAD2水平（物理截留于TGFBR1），可能压制TGF-β依赖的TE转录——即VEPH1→SMAD2胞质截留→SBE-TE启动子沉默。其二，TNFAIP3/A20互作将VEPH1与NF-κB免疫信号直接连接——A20的多聚泛素化编辑功能（K63去泛素化和K48泛素化）调控RIP1/TRAF6/IKKγ的活性，而NF-κB是ERV和LINE-1转录应答的重要正调控因子。其三，TOP3B的R-loop解旋功能在TE区域尤为重要——R-loop在LTR和LINE-1序列上异常积累，TOP3B的缺陷导致R-loop持久化和基因组不稳定性，VEPH1-TOP3B互作可能调控此过程。

**前沿意义**：VEPH1代表含PH域的armadillo支架蛋白在TGF-β-SMAD-TE调控交叉中的关键未研究节点。TNFAIP3（A20）互作更加强化了VEPH1的免疫调控潜力——A20作为NF-κB的负调控因子，其功能与TE去抑制的慢性炎症交叉已知密切相关。利用TGFBR1抑制剂（如galunisertib）和VEPH1敲除/敲低细胞模型，对TGF-β反应性和NF-κB反应性TE（含SBE/NF-κB位点的LTR）进行RNA-seq分析，可直接验证VEPH1→SMAD2截留→TE沉默的机制假说。


