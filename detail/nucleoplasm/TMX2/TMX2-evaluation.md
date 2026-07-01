---
type: protein-evaluation
gene: "TMX2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMX2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMX2 |
| 蛋白名称 | Thioredoxin-related transmembrane protein 2 |
| 蛋白大小 | 296 aa / 34.0 kDa |
| UniProt ID | Q9Y320 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 296 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=35 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=85.8; PDB=2 |
| 调控结构域 | 4/10 | x2 | 8.0 | Thioredoxin-like_sf; Thioredoxin_domain; TMX2 |
| PPI | 8/10 | x3 | 24.0 | PPI degree=224 |
| **加权总分** | | | **139/180** | |
| **归一化总分** | | | **77.0/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=35 broad=48
- AF pLDDT=85.8 PDB=2
- InterPro: Thioredoxin-like_sf; Thioredoxin_domain; TMX2
- Pfam: Thioredoxin
- PPI degree=224 ChIP: None
38797513: TMX2 potentiates cell viability of hepatocellular carcinoma by promoting autopha | 32878123: Thioredoxin-Related Transmembrane Proteins: TMX1 and Little Brothers TMX2, TMX3, | 41175374: The ER thioredoxin-related transmembrane protein TMX2 controls redox-mediated te

### 4. 总体评价
**77.0/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**结构域架构**: TMX2的核心功能模块是硫氧还蛋白结构域（Thioredoxin domain, IPR013766/PF00085），采用经典的βαββαββα折叠拓扑，活性位点为保守的CXXC二硫键氧化还原基序（通常为CGPC或CPPC）。该结构域属于硫氧还蛋白样超家族（Thioredoxin-like_sf, IPR036249），与蛋白质二硫键异构酶（PDI）家族共享折叠骨架。TMX2特异性结构域（IPR039101, IPR037463）将这个蛋白与TMX1、TMX3、TMX4区分开来——这些家族特异性区域可能决定了其独特的亚细胞定位（ER-线粒体接触位点）和底物选择性。UniProt功能注释明确指出TMX2是一个内质网和线粒体相关蛋白，"transmembrane"命名暗示存在一个N端跨膜螺旋将其锚定在ER膜上，活性硫氧还蛋白结构域面向细胞质或膜间隙。

**PPI网络解读**: TMX2的PPI网络（degree=224）是五个候选蛋白中最广泛的，反映了其多区室（ER、线粒体、核质）功能。HNRNPU（BioGRID）是核基质/RNA结合蛋白——与核质的直接联系，提示TMX2通过HNRNPU参与核基质组织或RNA加工。SRSF5（BioGRID）是SR蛋白家族的精氨酸/丝氨酸富集剪接因子——其活性受磷酸化严格调控，而磷酸化状态本身可被氧化还原信号调控。TMX2可能通过调节SRSF5关键半胱氨酸残基的氧化还原状态，间接调控选择性剪接。ATXN1（BioGRID）是脊髓小脑性共济失调1型的致病蛋白——这一互作提示TMX2在神经退行性疾病背景下可能调节ATXN1的折叠或聚集。ABCC1（BioGRID）是MRP1多药耐药转运蛋白，提示TMX2可能影响肿瘤细胞的氧化还原稳态和化疗耐药。

**结构诠释**: AlphaFold pLDDT=85.8且存在2个PDB条目，表明TMX2的结构已有实验验证。硫氧还蛋白结构域的核心βαββαββα折叠高度保守，CXXC基序位于β1和α2之间的环区（N端），使其暴露于溶剂以便与底物蛋白的半胱氨酸进行二硫键交换。两个PDB条目很可能分别捕获了氧化态（二硫键形成）和还原态（两个游离硫醇）的构象——这二者的结构差异通常体现在活性位点环的构象变化上。中等的pLDDT（85.8而非95+）提示跨膜螺旋和连接区域的柔性，这些区域可能介导与不同膜接触位点蛋白的动态互作。

**分子机制模型**: TMX2在三层膜界面操作：(1) 在ER-线粒体接触位点，TMX2通过硫氧还蛋白结构域催化氧化还原介导的栓系（PMID 41175374, Cell Rep 2025），可能通过调控MFN2或其他栓系蛋白的关键二硫键状态来控制接触位点的形成与解离；(2) 在ER腔内，TMX2作为氧化还原酶参与新生蛋白的氧化折叠——与PDI家族成员协同作用，但通过其独特的跨膜锚定实现空间特异性；(3) 在核质中（HPA Approved），TMX2通过HNRNPU和SRSF5参与剪接因子的氧化还原调控，影响pre-mRNA的选择性剪接。PMID 32878123的系统综述建立了TMX家族的功能框架，指出TMX2是ER蛋白质量控制网络的关键节点。PMID 38797513（HCC细胞活力）揭示了TMX2通过自噬通路促进肝细胞癌存活——氧化还原敏感的硫氧还蛋白结构域可能作为ER应激与自噬启动之间的分子开关。

**研究/治疗意义**: TMX2代表了氧化还原调控与膜接触位点生物学的交叉点。在肝细胞癌中（PMID 38797513），TMX2可能通过维持ER-线粒体接触位点的完整性来促进线粒体能量代谢和自噬平衡——TMX2的过表达可能是肿瘤细胞适应氧化应激的机制。在神经系统发育中（PMID 40891441，斑马鱼Tmx2b敲除导致神经元死亡），TMX2的氧化还原活性对神经元存活是必需的——这提示TMX2在人类神经发育障碍和神经退行性疾病中具有潜在意义。药理学上，硫氧还蛋白结构域是已确立的药物靶点类型（如金诺芬靶向TrxR），针对TMX2特异性的抑制（利用TMX2特异性结构域IPR039101/37进行选择性设计）可能避免影响其他硫氧还蛋白家族成员。核质功能（剪接调控）提示TMX2抑制剂可能通过影响选择性剪接模式间接调控基因表达。

### 补充分析 (UniProt API)

**蛋白全称**: Thioredoxin-related transmembrane protein 2

**功能**: Endoplasmic reticulum and mitochondria-associated protein that probably functions as a regulator of cellular redox state and thereby regulates protein post-translational modification, protein folding and mitochondrial activity. Indirectly regulates neuronal proliferation, migration, and organization in the developing brain

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR036249 |
| InterPro | IPR013766 |
| InterPro | IPR039101 |
| InterPro | IPR037463 |
| Pfam | PF00085 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| COMMD8 | BioGRID | 0 |
| ABCC1 | BioGRID | 0 |
| HNRNPU | BioGRID | 0 |
| TM9SF4 | BioGRID | 0 |
| SRSF5 | BioGRID | 0 |
| ATXN1 | BioGRID | 0 |
| SRPRB | BioGRID | 0 |
| HSD11B1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y320-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 48**

| 41948934 | Vancomycin eliminates gut deoxycholic acid, restoring ER proteostasis in ILC2s and relieving colitis. | JCI Insight 2026 |
| 41175374 | The ER thioredoxin-related transmembrane protein TMX2 controls redox-mediated tethering of ER-mitochondria contacts. | Cell Rep 2025 |
| 40891441 | The non-canonical thioreductase Tmx2b is essential for neuronal survival during zebrafish embryonic brain development. | Development 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMX2

