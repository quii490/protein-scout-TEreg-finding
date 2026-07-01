---
type: protein-evaluation
gene: "SYNJ2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SYNJ2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SYNJ2 |
| 蛋白名称 | Polyphosphatidylinositol phosphatase SYNJ2 |
| 蛋白大小 | 1496 aa / 165.5 kDa |
| UniProt ID | O15056 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | nan (Approved) |
| 蛋白大小 | 6/10 | ×1 | 6.0 | 1496 aa |
| 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=30 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=67.6; PDB=1 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Endo/exonu/phosph_ase_sf; IP5; IPPc |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=78 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
- HPA: nan (Approved)
- PubMed: strict=30, broad=41
- AF pLDDT: 67.6 / PDB: 1
- InterPro: Endo/exonu/phosph_ase_sf; IP5; IPPc
- Pfam: DUF1866; Exo_endo_phos2; Syja_N
- PPI degree: 78 / ChIP: None
**Papers**: 35216662: Neuronal mitochondria transport Pink1 mRNA via synaptojanin 2 to support local m | 41955750: Synaptojanin-2-binding protein ameliorates oxidative stress, neuroinflammation a | 38504131: Insulin signalling regulates Pink1 mRNA localization via modulation of AMPK acti

### 4. 总体评价
★★★★  **72.7/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Polyphosphatidylinositol phosphatase SYNJ2

**功能**: Phosphatase that hydrolyzes phosphate groups from the inositol ring of phosphoinositides and inositol phosphates, in a domain-specific manner (PubMed:11084340, PubMed:12699622, PubMed:40969890). The 5-PPase domain catalyzes removal of the 5-phosphate from substrates such as phosphatidylinositol-4,5-bisphosphate (PtdIns(4,5)P2), phosphatidylinositol-3,4,5-trisphosphate (PtdIns(3,4,5)P3), inositol-1,4,5-trisphosphate (Ins(1,4,5)P3) and inositol-1,3,4,5-tetrakisphosphate (Ins(1,3,4,5)P4) (PubMed:11

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR036691 |
| InterPro | IPR046985 |
| InterPro | IPR000300 |
| InterPro | IPR012677 |
| InterPro | IPR035979 |
| InterPro | IPR000504 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SFN | BioGRID | 0 |
| SYNJ2BP | BioGRID | 0 |
| RAC1 | BioGRID | 0 |
| GRB2 | BioGRID | 0 |
| ITSN2 | BioGRID | 0 |
| ITSN1 | BioGRID | 0 |
| SH3KBP1 | BioGRID | 0 |
| CDH1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O15056-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 41**

| 42281968 | Non-coding Regulatory Variants in ASD (Autism Spectrum Disorders) Disrupt CTCF Domains and Shape Cell-Type-Specific Neur | Res Sq 2026 |
| 41955750 | Synaptojanin-2-binding protein ameliorates oxidative stress, neuroinflammation and depression-like behaviors via SYNJ2/P | Redox Biol 2026 |
| 41173111 | Insights into transcriptomic changes in blood of a mouse model of LPS-induced peritonitis. | Toxicol Appl Pharmacol 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SYNJ2


### 深度机制分析

SYNJ2（Synaptojanin-2）是一个大型双功能磷酸肌醇磷酸酶（1496 aa, 165.5 kDa），其结构架构集成了两种截然不同的催化活性：5-磷酸酶（5-PPase）结构域和Sac1-like磷酸酶结构域。InterPro结构域图谱显示Endo/exonu/phosph_ase_sf（IPR036691）构成了5-PPase催化核心，IP5结构域（IPR046985, SYNJ2特有）和IPPc结构域（IPR000300, 肌醇多磷酸磷酸酶催化域）组成了完整的催化模块。Pfam进一步将结构域解析为DUF1866（N端辅助结构域）、Exo_endo_phos2（5-PPase催化域, PF03372）和Syja_N（N端Sac结构域, PF02383）。AlphaFold预测pLDDT=67.6偏低，这主要是由于1496个残基中存在大量长程柔性连接区段（linker regions），连接区段本身缺乏三维结构约束，但5-PPase和Sac1催化核心的局部折叠质量应明显高于全局平均值。

5-PPase结构域催化水解PtdIns(4,5)P2的5-磷酸、PtdIns(3,4,5)P3的5-磷酸以及Ins(1,4,5)P3的5-磷酸（PubMed:11084340, PubMed:12699622, PubMed:40969890）。同时，Sac1-like结构域水解PtdIns(4)P、PtdIns(3)P和PtdIns(3,5)P2的磷酸单酯键。这两个结构域的组合赋予了SYNJ2同时降解多种磷酸肌醇信号分子的独特能力——相当于磷酸肌醇通路的"信号终止器"（signal terminator）。PPI互作网络（degree=78）核心参与者包括RAC1（Rho GTPase, 肌动蛋白骨架调控）、GRB2（生长因子受体衔接蛋白）、ITSN1/ITSN2（intersectin, 内吞衔接蛋白）、SH3KBP1（CIN85, 内吞多功能衔接体）、CDH1（E-cadherin）、SFN（14-3-3 sigma, 磷酸化蛋白结合因子）以及SYNJ2BP（特异结合伴侣）。

SYNJ2最独特的细胞功能是通过锚定在线粒体外膜的SYNJ2BP（SYNJ2 binding protein）介导Pink1 mRNA的线粒体靶向运输。PMID:35216662和PMID:38504131揭示了这一分子机制的完整路径：胰岛素信号→AMPK活化→SYNJ2磷酸化→SYNJ2-SYNJ2BP互作增强→Pink1 mRNA在线粒体表面的富集→Pink1蛋白的局部翻译→线粒体自噬（mitophagy）启动。这一"局部mRNA运输-翻译"机制确保了Pink1蛋白在其功能位点（线粒体外膜）的高效生产，是神经保护的核心路径。

核定位方面，HPA标注SYNJ2定位为"Approved"但具体核定位信号不明确（报告标注为nan）。SYNJ2的核内功能文献极为有限——该蛋白的主要功能空间是胞质内吞/外排系统（endocytic/exocytic system）、线粒体表面和细胞骨架。综合来看，SYNJ2的深度机制模型为：5-PPase+Sac1双磷酸酶→PtdIns(4,5)P2/PtdIns(3,4,5)P3信号终止→Pink1 mRNA线粒体靶向（AMPK依赖）→线粒体自噬神经保护；次要功能：RAC1-GRB2-ITSN内吞复合体调控→囊泡运输。该蛋白通过Pink1/线粒体自噬间接参与神经保护和氧化应激响应，但其直接参与核内TE调控的证据极为薄弱。



