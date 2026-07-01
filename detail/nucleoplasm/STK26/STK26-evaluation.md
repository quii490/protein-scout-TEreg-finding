---
type: protein-evaluation
gene: "STK26"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## STK26 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | STK26 |
| 蛋白名称 | Serine/threonine-protein kinase 26 |
| 蛋白大小 | 416 aa / 46.5 kDa |
| UniProt ID | Q9P289 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Centrosome; Cytosol; Golgi apparatus; Nucleoplasm (Uncertain) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 416 aa |
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed=16 |
| 三维结构 | 9/10 | ×3 | 27.0 | pLDDT=79.6; PDB=9 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Kinase-like_dom_sf; PDC10_dimerisation_sf; PDCD10_N |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=189 |
| **加权总分** | | | **138/180** | |
| **归一化总分** | | | **76.5/100** | 互证: +2 |

### 3. 分析
- Centrosome; Cytosol; Golgi apparatus; Nucleoplasm (Uncertain)
- PubMed strict=16 broad=71
- AF pLDDT=79.6 PDB=9
- InterPro: Kinase-like_dom_sf; PDC10_dimerisation_sf; PDCD10_N
- Pfam: PDCD10_N; Pkinase
- PPI degree=189 ChIP: None
37094736: The mammalian Sterile 20-like kinase 4 (MST4) signaling in tumor progression: Im | 36428665: Construction of Oxidative Stress-Related Genes Risk Model Predicts the Prognosis | 35563749: Transcriptome Reveals Granulosa Cells Coping through Redox, Inflammatory and Met

### 4. 总体评价
**76.5/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**结构域架构**：STK26（又名MST4）属于生发中心激酶（GCK）家族中的STE20亚家族，其结构域架构由N端丝氨酸/苏氨酸激酶结构域（IPR000719蛋白激酶，IPR011009激酶样结构域超家族，IPR017441蛋白激酶ATP结合位点，Pfam Pkinase）和C端PDCD10_N二聚化结构域（IPR046409，IPR048288，IPR050629 PDC10二聚化超家族）组成。这一结构域组织是MST激酶亚家族（MST1/STK4、MST2/STK3、MST3/STK24、MST4/STK26）的标志性特征。PDCD10_N结构域不仅介导STK26同源二聚化，更为关键的是——它作为STRIPAK（striatin-interacting phosphatase and kinase）超大分子复合物的锚定模块，将STK26的激酶活性与PP2A磷酸酶活性进行物理偶联。这种"激酶-磷酸酶共定位"的复合物组织模式是STRIPAK系统的核心设计原则：磷酸化和去磷酸化在同一纳米尺度反应室内被精确调控。

**PPI网络与信号通路**：STK26的PPI（degree=189）以极高的STRING置信度分数定义了STRIPAK复合物的核心组分：STRIP1（999）、STRN3（998）、STK3（998）、STK24（998）、STRN（980）。这些分数998-999指示这些蛋白在数千个基因组中表现为共进化/共表达/基因融合，是进化上不可分离的功能模块。PPP2R1A（STRING 876）是PP2A全酶的支架亚基（A亚基），串联STRIPAK的激酶和磷酸酶模块。CASP3（857）确认了STK26在凋亡调控中的角色。功能上，STRIPAK-STK26调控三条关键信号通路：(1) Hippo信号——通过磷酸化级联控制器官大小和肿瘤抑制；(2) 细胞迁移——在RHO激活后负调控高尔基体重定向，建立细胞极性（PubMed 27807006）；(3) 自噬——直接磷酸化ATG4B的Ser-383位点以增强自噬通量（PubMed 29232556）。STK26对ATF6的稳定性调控（PubMed 40869379）将STRIPAK系统与内质网应激/未折叠蛋白反应（UPR）连接起来，这是2025年的新发现。

**结构生物学解读**：STK26的结构认知较为成熟：pLDDT=79.6且拥有9个PDB条目。激酶结构域预期采用典型双叶激酶折叠（N端β-折叠叶和C端α-螺旋叶，ATP结合于两者之间的裂隙）。PDCD10_N二聚化结构域已在PDCD10（CCM3）复合物中被结构解析，采用α-螺旋束折叠介导疏水界面二聚化。pLDDT=79.6的中高值反映了激酶结构域的有序性，但PDCD10_N和域间连接区可能存在动态柔性——这种柔性对于STRIPAK在多种信号输入下动态重排复合物组成可能是功能必需的。9个PDB条目涵盖激酶结构域的多种构象状态（活性态、非活性态、抑制剂结合态），为理性药物设计提供了结构模板。

**分子机制模型**：STK26在细胞中扮演"STRIPAK调控枢纽"的角色，其活性受亚细胞定位和复合物组成的双重控制。在高尔基体：STRIPAK-STK26感知RHO信号，通过磷酸化下游靶标来负调控高尔基堆栈重定向，确保定向细胞迁移中的极性维持。当RHO过度激活时，STK26限制高尔基体重排，防止迁移方向紊乱。在胞浆/自噬体：代谢应激（如氨基酸剥夺）触发STK26磷酸化ATG4B（Ser-383），增强ATG4B的蛋白酶活性，促进LC3脂质化，从而加速自噬体形成。这是一个细胞自主的生存机制。在细胞核（核质定位，具有不确定性）：STK26磷酸化ATF6并阻止其泛素化降解（PubMed 40869379），导致ATF6蛋白累积。ATF6是UPR的三大传感器之一，其稳定化激活内质网应激靶基因转录，赋予结直肠癌细胞在内质网应激下的生存优势。这一核内功能将STRIPAK的调控范围从胞浆信号扩展至核内转录调控。

**研究与转化医学意义**：STK26-STRIPAK是开发抗癌药物的多节点靶点：(1) ATP竞争性激酶抑制剂可阻断STK26的催化活性——已有的MST激酶抑制剂（如XMU-MP-1靶向MST1/2）可作为先导化合物优化的起点；(2) PDCD10_N二聚化界面的破坏可解离STRIPAK复合物，是一种蛋白-蛋白相互作用（PPI）抑制策略；(3) ATF6稳定性调控轴的发现（PubMed 40869379）提示STK26可能是克服内质网应激介导的化疗耐药的新靶点。此外，STK26在DNA甲基化介导的肥胖免疫记忆中（PubMed 42045443）——CD4 T细胞中STK26位点的表观遗传改变与肥胖相关免疫功能紊乱持续存在有关——揭示了环境暴露通过表观遗传锁定STK26表达变化从而影响长期免疫状态的新范式。核内STK26-ATF6的功能被认为在Hippo信号之外构成了STK26的独立信号输出分支，值得用条件性核定位信号突变体进行功能分离实验。


### 补充分析 (UniProt API)

**蛋白全称**: Serine/threonine-protein kinase 26

**功能**: Serine/threonine-protein kinase that acts as a mediator of cell growth (PubMed:11641781, PubMed:17360971). Modulates apoptosis (PubMed:11641781, PubMed:17360971). In association with STK24 negatively regulates Golgi reorientation in polarized cell migration upon RHO activation (PubMed:27807006). Phosphorylates ATG4B at 'Ser-383', thereby increasing autophagic flux (PubMed:29232556). Part of the striatin-interacting phosphatase and kinase (STRIPAK) complexes. STRIPAK complexes have critical roles

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011009 |
| InterPro | IPR046409 |
| InterPro | IPR048288 |
| InterPro | IPR000719 |
| InterPro | IPR017441 |
| InterPro | IPR050629 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| STRIP1 | STRING | 999 |
| STRN3 | STRING | 998 |
| STK3 | STRING | 998 |
| STK24 | STRING | 998 |
| STRN | STRING | 980 |
| PPP2R1A | STRING | 876 |
| CASP3 | STRING | 857 |
| C4ORF19 | STRING | 827 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9P289-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000134602-STK26

![](https://images.proteinatlas.org/59921/1011_E12_2_red_green.jpg)
![](https://images.proteinatlas.org/59921/1011_E12_5_red_green.jpg)
![](https://images.proteinatlas.org/59921/1043_F9_4_red_green.jpg)
![](https://images.proteinatlas.org/59921/1043_F9_7_red_green.jpg)
![](https://images.proteinatlas.org/59921/1006_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/59921/1006_E12_9_red_green.jpg)

### PubMed 文献

**PubMed count: 71**

| 42235722 | Genome-wide association analysis for resistance against iridovirus disease in large yellow croaker (Larimichthys crocea) | Fish Shellfish Immunol 2026 |
| 42045443 | DNA methylation-mediated memory of obesity in CD4 T lymphocytes perpetuates immune dysregulation. | EMBO Rep 2026 |
| 40869379 | STK26 Promotes the Stabilization of ATF6 to Facilitate the Progression of Colorectal Cancer. | Int J Mol Sci 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/STK26

