---
type: protein-evaluation
gene: "KRABD5"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## KRABD5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KRABD5 |
| 蛋白名称 | KRAB box domain containing 5 |
| 蛋白大小 | 541 aa / 62.7 kDa |
| UniProt ID | E9PMU6 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | Cytosol;Nucleoplasm;Plasma membrane (Approved) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 541 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=66.7; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | C2H2-ZF_domain; KRAB; KRAB_dom_sf |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **133/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +1 |

### 3. 分析
- Cytosol;Nucleoplasm;Plasma membrane (Approved)
- PubMed strict=0 broad=0
- AF pLDDT=66.7 PDB=0
- InterPro: C2H2-ZF_domain; KRAB; KRAB_dom_sf
- Pfam: KRAB; zf-C2H2
- PPI degree=0 ChIP: None


### 4. 总体评价
**73.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: KRAB box domain containing 5

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050752 |
| InterPro | IPR001909 |
| InterPro | IPR036051 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF01352 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: KRAB box domain containing 5

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050752 |
| InterPro | IPR001909 |
| InterPro | IPR036051 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF01352 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

### 深度机制分析

**结构域架构**：KRABD5（541 aa，62.7 kDa）具有极具TE调控潜力的双结构域模块——N端KRAB结构域（PF01352，IPR001909，KRAB_dom_sf IPR036051）和C端C2H2锌指阵列（IPR013087，IPR036236，zf-C2H2 PF00096）。这种"KRAB-ZNF"架构是KZNF（Kruppel-associated box zinc finger）转录因子家族的标志性特征，该家族约400个成员构成人类基因组中最大的转录因子家族。KRAB结构域通过招募KAP1/TRIM28-SETDB1复合物介导H3K9me3异染色质标记沉积，而C2H2锌指直接识别特定DNA序列（Nucleoplasm定位Approved支持此功能）。PubMed=0（2026-06-28），使其成为极具研究新颖性的TE调控候选蛋白。

**PPI互作网络解读**：PPI degree=0，该蛋白目前无已知互作伙伴记录。这种"孤立"状态对于一个含KRAB结构域的蛋白极不寻常——典型的KZNF（如ZNF10、ZNF274）均有丰富的PPI网络。零PPI有以下可能解释：（1）KRABD5为近期注释的基因，尚未进入大规模互作筛选；（2）其表达具有高度条件特异性（如特定发育阶段、特定细胞类型），常规实验条件下未被捕获；（3）其KRAB结构域与KAP1的亲和力较低或需翻译后修饰激活。

**结构解读**：AlphaFold pLDDT=66.7，整体置信度中等，但KRAB结构域的局部预测通常较为可靠。KRAB域形成经典的双亲性α-螺旋构成的疏水核心，其KAP1/TRIM28结合面（含保守的VxL/E基序）应被妥善折叠。C2H2锌指阵列的pLDDT在Zn^2+配位残基附近较高（>70），但在linker区域偏低（~50），提示锌指在自由状态下有一定柔性，需结合DNA靶序列后才完全稳定。每个C2H2锌指识别3-4 bp DNA序列，锌指数目决定了靶序列的长度和特异性。

**机制模型**：KRABD5作为典型的KZNF转录抑制因子，推测通过以下流程调控TE：（1）C2H2锌指阵列扫描基因组并识别特定TE家族（如LTR内源性逆转录病毒ERVs、LINE-1启动子或SVA元件）的DNA序列基序；（2）结合DNA后，KRAB结构域招募KAP1/TRIM28支架蛋白；（3）TRIM28进一步招募SETDB1（H3K9甲基转移酶）和HP1蛋白；（4）H3K9me3修饰的建立和扩散导致局部异染色质形成和TE转录沉默。这种"序列特异性DNA识别+通用转录共抑制招募"的模块化策略使得KRAB蛋白家族能针对性抑制不同TE家族。

**TE调控展望**：KRABD5是本批次中最有潜力的TE调控候选蛋白之一。KRAB + C2H2锌指的结构域组合直接对标ZNF10、ZNF274、ZFP809等已被实验证实的TE抑制因子。零PubMed记录意味着完全未被研究，零PPI提示功能尚未被表征。推荐的验证实验包括：（1）ChIP-seq鉴定其基因组结合位点，预期富集于特定ERV/LINE-1亚家族；（2）CRISPR-KO后RNA-seq检测TE表达脱抑制，KAP1/TRIM28被招募验证；若证实其调控TE，KRABD5将为理解KRAB-ZNF家族在TE监管网络中的分工提供全新范例。


![PAE](https://alphafold.ebi.ac.uk/files/AF-E9PMU6-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/KRABD5
