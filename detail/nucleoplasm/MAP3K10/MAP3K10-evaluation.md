---
type: protein-evaluation
gene: "MAP3K10"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## MAP3K10 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MAP3K10 |
| 蛋白名称 | Mitogen-activated protein kinase kinase kinase 10 |
| 蛋白大小 | 954 aa / 103.7 kDa |
| UniProt ID | Q02779 |
| 评估日期 | 2026-06-27 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Actin filaments; Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 954 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=22 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=60.3; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | Kinase-like_dom_sf; MLK1-3_SH3; MLK1-4 |
| PPI | 6/10 | x3 | 18.0 | PPI degree=56 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +2 |
### 3. 分析
- HPA: Actin filaments; Cytosol; Nucleoplasm (Approved)
- PubMed: strict=22, broad=74
- AF pLDDT: 60.3 / PDB: 1
- InterPro: Kinase-like_dom_sf; MLK1-3_SH3; MLK1-4
- Pfam: PK_Tyr_Ser-Thr; SH3_9
- PPI degree=56 / ChIP: None
36341729: DNA methylation of the MAP3K10 gene may participate in the development of intrac | 31954518: Methionine stimulates GlyRS phosphorylation via the GPR87-CDC42/Rac1-MAP3K10 sig | 23760366: The TGFβ-induced phosphorylation and activation of p38 mitogen-activated protein
### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

MAP3K10（又称MLK2）作为混合谱系激酶家族成员，通过其N端SH3结构域（IPR035779/MLK1-3_SH3）与C端激酶结构域（IPR000719/PK_Tyr_Ser-Thr）的协同作用，在JNK信号通路的层级磷酸化中充当关键节点。其954个氨基酸的多结构域架构赋予该蛋白独特的支架与催化双重功能：SH3结构域介导与上游激活因子（如CDC42、RAC1）的蛋白-蛋白互作（PPI degree=56），而激酶结构域则通过磷酸化MKK4/MKK7进而激活JUN N-terminal pathway。AlphaFold预测的整体pLDDT为60.3，提示蛋白含有较高比例的内在无序区域（IDR），这些柔性区段可能作为分子开关参与信号复合体的动态组装与解聚。

MAP3K10的核定位（HPA Approved: Nucleoplasm）与经典膜相关/细胞骨架定位（Actin filaments; Cytosol）的共存提示其存在非经典的核质穿梭机制。该蛋白无经典的核定位信号（NLS），暗示其入核可能依赖与含NLS的伙伴蛋白（如NEUROD1、KIF17）的"搭载"转运，或通过SH3结构域识别核孔复合体组分。值得注意的是，PPI网络中KIF17与KIF3A均为驱动蛋白家族成员，涉及沿微管的定向运输——该机制可能同时服务于MAP3K10的胞质骨架定位与核周富集。

从结构生物学角度看，MAP3K10拥有1个PDB条目但覆盖度有限，反映了其多结构域串联构象的解析难度。激酶结构域的催化活性受SH3结构域自抑制调控——静息态下SH3可能通过分子内相互作用遮蔽激酶活性位点；RAC1/CDC42结合后解除自抑制，触发下游级联。已报道的DNA甲基化调控（PMID:36341729）进一步提示MAP3K10的表达受表观遗传修饰精细控制，而GPR87-CDC42/Rac1-MAP3K10信号轴（PMID:31954518）则在甲硫氨酸感应中连接代谢信号至MAPK通路。

MAP3K10作为JNK信号的核心调控器，其核定位暗示可能通过磷酸化核内转录因子（如c-Jun）直接参与基因表达调控。TGF-beta通路中MAP3K10对p38的磷酸化激活（PMID:23760366）进一步拓展了其在应激响应中的功能谱。鉴于MLK家族在肿瘤发展与血管生成中的已知角色（PMID:40314847），MAP3K10的核质双重定位可能成为肿瘤治疗的新靶点——核内池的MAP3K10可能驱动促增殖转录程序，而胞质池则调控细胞骨架动力学与迁移。

**蛋白全称**: Mitogen-activated protein kinase kinase kinase 10

**功能**: Activates the JUN N-terminal pathway

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011009 |
| InterPro | IPR035779 |
| InterPro | IPR016231 |
| InterPro | IPR000719 |
| InterPro | IPR017441 |
| InterPro | IPR001245 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NEUROD1 | BioGRID | 0 |
| CDC42 | BioGRID | 0 |
| RAC1 | BioGRID | 0 |
| KIF17 | BioGRID | 0 |
| KIF3A | BioGRID | 0 |
| KIFAP3 | BioGRID | 0 |
| YWHAE | BioGRID | 0 |
| HPCA | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q02779-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 74**

| 41102374 | Integrated machine learning identifies biomarkers for bilirubin-induced Alzheimer's disease-like lesions in neonates and | Sci Rep 2025 |
| 40582529 | Transcriptomic analysis reveals the role of MAPK signaling pathway in IgM(+) B cells against Pseudomonas plecoglossicida | Fish Shellfish Immunol 2025 |
| 40314847 | Mixed lineage kinase (MLK) controls tumor development and angiogenesis. | Angiogenesis 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/MAP3K10

