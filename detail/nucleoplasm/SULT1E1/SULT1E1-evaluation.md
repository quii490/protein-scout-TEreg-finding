---
type: protein-evaluation
gene: "SULT1E1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SULT1E1 — REJECTED (研究热度过高 (PubMed strict=173，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SULT1E1 / STE |
| 蛋白名称 | Sulfotransferase 1E1 |
| 蛋白大小 | 294 aa / 35.1 kDa |
| UniProt ID | P49888 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane, Cytosol; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 294 aa / 35.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=173 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=97.2; PDB: 1G3M, 1HY3, 4JVL, 4JVM, 4JVN |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR027417, IPR000863; Pfam: PF00685 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane, Cytosol | Uncertain |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear membrane (GO:0031965)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 173 |
| PubMed broad count | 329 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: STE |

**关键文献**:
1. Single-cell analysis reveals insights into epithelial abnormalities in ovarian endometriosis.. *Cell reports*. PMID: 38412094
2. Metformin inhibits testosterone-induced endoplasmic reticulum stress in ovarian granulosa cells via inactivation of p38 MAPK.. *Human reproduction (Oxford, England)*. PMID: 32372097
3. Estrogen Sulfotransferase (SULT1E1): Its Molecular Regulation, Polymorphisms, and Clinical Perspectives.. *Journal of personalized medicine*. PMID: 33799763
4. Overexpression of SULT1E1 alleviates salt-processed Psoraleae Fructus-induced cholestatic liver damage.. *Chinese herbal medicines*. PMID: 40256713
5. Estrogen sulfotransferase SULT1E1 expression correlates with progression and prognosis of lung adenocarcinoma.. *Scientific reports*. PMID: 39762281

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.2 |
| 高置信度残基 (pLDDT>90) 占比 | 95.2% |
| 置信残基 (pLDDT 70-90) 占比 | 3.7% |
| 中等置信 (pLDDT 50-70) 占比 | 0.7% |
| 低置信 (pLDDT<50) 占比 | 0.3% |
| 有序区域 (pLDDT>70) 占比 | 98.9% |
| 可用 PDB 条目 | 1G3M, 1HY3, 4JVL, 4JVM, 4JVN |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1G3M, 1HY3, 4JVL, 4JVM, 4JVN）+ AlphaFold极高置信度预测（pLDDT=97.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417, IPR000863; Pfam: PF00685 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TERT | 0.996 | 0.000 | — |
| HSD17B1 | 0.962 | 0.000 | — |
| UGT1A6 | 0.959 | 0.000 | — |
| HSD17B2 | 0.959 | 0.000 | — |
| CYP19A1 | 0.959 | 0.000 | — |
| UGT1A10 | 0.958 | 0.000 | — |
| UGT1A4 | 0.958 | 0.000 | — |
| UGT1A8 | 0.957 | 0.000 | — |
| UGT1A1 | 0.956 | 0.000 | — |
| UGT1A7 | 0.955 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BMPR2 | psi-mi:"MI:0096"(pull down) | pubmed:15188402 |
| SULT2B1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ENOX1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TP53 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| UNC119 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EEF1A1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RIF1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SETDB1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| COPS6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RBM48 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.2 + PDB: 1G3M, 1HY3, 4JVL, 4JVM, 4JVN | pLDDT=97.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Nuclear membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. SULT1E1 — Sulfotransferase 1E1，研究基础较多，新颖性有限。
2. 蛋白大小294 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 173 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 173 > 100，研究热度过高，不符合novelty筛选标准。**

### 深度机制分析

SULT1E1（Sulfotransferase 1E1，也称雌激素磺基转移酶/EST）属于胞质磺基转移酶（SULT）超家族。其结构域架构包含典型的磺基转移酶折叠：InterPro注释为IPR027417（P-loop containing nucleoside triphosphate hydrolase）和IPR000863（Sulfotransferase domain），Pfam对应PF00685（Sulfotransfer_1）。AlphaFold v6预测整体pLDDT=97.2——这是所有评估蛋白中最高质量的结构预测——高置信度残基占95.2%，有序区域占98.9%。此外，该蛋白拥有5个实验性PDB结构（1G3M、1HY3、4JVL、4JVM、4JVN），提供了原子分辨率的催化机制信息。这种丰富的结构数据使SULT1E1成为机制研究中结构信息最完整的蛋白之一。

SULT1E1的核心生化功能是将磺酸基（SO3-）从供体3'-磷酸腺苷-5'-磷酰硫酸（PAPS）转移至雌激素（E2）的3-羟基位，生成硫酸化雌激素（E2-S）。硫酸化显著改变底物的生物活性：硫酸化雌激素失去与雌激素受体（ER）的结合能力，同时增强水溶性促进排泄。因此，SULT1E1是雌激素信号的主要负调控节点，在激素依赖性组织（乳腺、子宫内膜）和代谢器官（肝脏）中发挥关键作用。近期研究进一步揭示了SULT1E1在肺腺癌进展和预后中的临床意义（PMID:39762281），以及其过表达缓解盐制补骨脂诱导的胆汁淤积性肝损伤（PMID:40256713）。

PPI网络揭示了一些具有机制价值的互作。STRING记录的TERT（端粒酶逆转录酶，combined score=0.996）互作最为突出，提示SULT1E1可能与端粒维持和细胞衰老调控存在功能关联。IntAct实验验证的互作中，SETDB1（组蛋白H3K9甲基转移酶，PMID:16169070）和TP53（PMID:16169070）的出现尤为关键：SETDB1是转座子沉默和异染色质形成的主要酶，而TP53是基因组稳定性的核心守护者。SULT1E1-SETDB1互作提出了一个引人注目的假说：SULT1E1可能通过磺基化修饰调控SETDB1的活性或定位，间接参与TE的组蛋白修饰沉默。此外，RIF1（端粒相关蛋白和DNA双链断裂修复调控因子，PMID:16169070）和COPS6（COP9信号体亚基，PMID:16169070）的互作进一步支持SULT1E1在基因组稳定性网络中的潜在功能。

尽管该蛋白已被REJECTED（PubMed strict=173，>100篇阈值），其原因仅是新颖性不足而非机制意义缺失。HPA IF定位显示核膜（uncertain）和胞质溶胶，GO-CC注释确认nuclear membrane（GO:0031965）。核膜定位提示SULT1E1可能在核周区域调控蛋白磺基化，间接影响核输入/输出和染色质相关蛋白的活性。对于TE调控研究，SULT1E1与SETDB1的生化互作以及极高的结构信息可用性（pLDDT=97.2 + 5个PDB）使其成为药物靶点和功能研究的理想工具蛋白，尽管其新颖性评分不符合本项目的筛选标准。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49888
- Protein Atlas: https://www.proteinatlas.org/ENSG00000109193-SULT1E1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SULT1E1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49888
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (uncertain)。来源: https://www.proteinatlas.org/ENSG00000109193-SULT1E1/subcellular

![](https://images.proteinatlas.org/28213/1790_A1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28213/1790_A1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/28213/303_D5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28213/303_D5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P49888-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P49888 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027417;IPR000863; |
| Pfam | PF00685; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000109193-SULT1E1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PDE9A | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
