---
type: protein-evaluation
gene: "MLH1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MLH1 — REJECTED (研究热度过高 (PubMed strict=3494，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MLH1 / COCA2 |
| 蛋白名称 | DNA mismatch repair protein Mlh1 |
| 蛋白大小 | 756 aa / 84.6 kDa |
| UniProt ID | P40692 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 756 aa / 84.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=3494 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=77.3; PDB: 3RBN, 4P7A, 5U5P, 6WBA, 6WBB, 6WBC, 7M60 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR014762, IPR013507, IPR036890, IPR032189, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chiasma (GO:0005712)
- chromosome (GO:0005694)
- late recombination nodule (GO:0005715)
- male germ cell nucleus (GO:0001673)
- membrane (GO:0016020)
- MutLalpha complex (GO:0032389)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3494 |
| PubMed broad count | 7347 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: COCA2 |

**关键文献**:
1. Cancer risk in 348 French MSH2 or MLH1 gene carriers.. *Journal of medical genetics*. PMID: 12624141
2. Functional analysis of human MLH1 variants using yeast and in vitro mismatch repair assays.. *Cancer research*. PMID: 17510385
3. A calibrated cell-based functional assay to aid classification of MLH1 DNA mismatch repair gene variants.. *Human mutation*. PMID: 36054288
4. Methylation Tolerance-Based Functional Assay to Assess Variants of Unknown Significance in the MLH1 and MSH2 Genes and Identify Patients With Lynch Syndrome.. *Gastroenterology*. PMID: 30998989
5. Mutant huntingtin protein induces MLH1 degradation, DNA hyperexcision, and cGAS-STING-dependent apoptosis.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 38498709

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.3 |
| 高置信度残基 (pLDDT>90) 占比 | 50.1% |
| 置信残基 (pLDDT 70-90) 占比 | 23.4% |
| 中等置信 (pLDDT 50-70) 占比 | 6.2% |
| 低置信 (pLDDT<50) 占比 | 20.2% |
| 有序区域 (pLDDT>70) 占比 | 73.5% |
| 可用 PDB 条目 | 3RBN, 4P7A, 5U5P, 6WBA, 6WBB, 6WBC, 7M60 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3RBN, 4P7A, 5U5P, 6WBA, 6WBB, 6WBC, 7M60）+ AlphaFold极高置信度预测（pLDDT=77.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR014762, IPR013507, IPR036890, IPR032189, IPR002099; Pfam: PF01119, PF13589, PF16413 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MLH3 | 0.999 | 0.986 | — |
| PMS1 | 0.999 | 0.935 | — |
| BRIP1 | 0.999 | 0.994 | — |
| BLM | 0.999 | 0.996 | — |
| EXO1 | 0.999 | 0.943 | — |
| MSH3 | 0.999 | 0.829 | — |
| MSH2 | 0.999 | 0.923 | — |
| PMS2 | 0.999 | 0.997 | — |
| MSH6 | 0.999 | 0.864 | — |
| FAN1 | 0.997 | 0.838 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| Sgf11 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Pez | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Fer2LCH | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| AP2B1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRIM29 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Shmt | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| sip1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| CG12933 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| eIF3j | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.3 + PDB: 3RBN, 4P7A, 5U5P, 6WBA, 6WBB,  | pLDDT=77.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. MLH1 — DNA mismatch repair protein Mlh1，研究基础较多，新颖性有限。
2. 蛋白大小756 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3494 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 3494 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P40692
- Protein Atlas: https://www.proteinatlas.org/ENSG00000076242-MLH1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MLH1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P40692
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000076242-MLH1/subcellular

![](https://images.proteinatlas.org/52707/809_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/52707/809_G11_2_red_green.jpg)
![](https://images.proteinatlas.org/52707/819_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/52707/819_G11_2_red_green.jpg)
![](https://images.proteinatlas.org/52707/826_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/52707/826_G11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P40692-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
