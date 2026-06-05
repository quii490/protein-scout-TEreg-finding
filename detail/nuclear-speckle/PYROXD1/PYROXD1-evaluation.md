---
type: protein-evaluation
gene: "PYROXD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PYROXD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PYROXD1 |
| 蛋白名称 | tRNA ligase complex-associated NAD(P)H dehydrogenase PYROXD1 |
| 蛋白大小 | 500 aa / 55.8 kDa |
| UniProt ID | Q8WU10 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: Nucleus; Cytoplasm, cytosol; Cytoplasm, myofibril, sarcomere |
| 蛋白大小 | 10/10 | ×1 | 10 | 500 aa / 55.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=88.7; PDB: 6ZK7, 8ORJ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR050260, IPR036188, IPR023753, IPR016156, IPR041 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **142.0/180** | |
| **归一化总分** | | | **78.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
| UniProt | Nucleus; Cytoplasm, cytosol; Cytoplasm, myofibril, sarcomere | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)
- sarcomere (GO:0030017)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 31 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Mechanistic basis for PYROXD1-mediated protection of the human tRNA ligase complex against oxidative inactivation.. *Nature structural & molecular biology*. PMID: 40069351
2. Myofibrillar myopathy in the genomic context.. *Journal of applied genetics*. PMID: 30203143
3. The FACT complex facilitates expression of lysosomal and antioxidant genes through binding to TFEB and TFE3.. *Autophagy*. PMID: 35230915
4. The oxidoreductase PYROXD1 uses NAD(P)(+) as an antioxidant to sustain tRNA ligase activity in pre-tRNA splicing and unfolded protein response.. *Molecular cell*. PMID: 33930333
5. Clinical, histological, and genetic characterization of PYROXD1-related myopathy.. *Acta neuropathologica communications*. PMID: 31455395

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.7 |
| 高置信度残基 (pLDDT>90) 占比 | 75.6% |
| 置信残基 (pLDDT 70-90) 占比 | 15.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.2% |
| 低置信 (pLDDT<50) 占比 | 6.2% |
| 有序区域 (pLDDT>70) 占比 | 90.6% |
| 可用 PDB 条目 | 6ZK7, 8ORJ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6ZK7, 8ORJ）+ AlphaFold高质量预测（pLDDT=88.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050260, IPR036188, IPR023753, IPR016156, IPR041575; Pfam: PF07992, PF18267 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UPRT | 0.843 | 0.834 | — |
| FDX1 | 0.623 | 0.336 | — |
| PIPOX | 0.621 | 0.406 | — |
| ACOD1 | 0.621 | 0.406 | — |
| DDO | 0.621 | 0.406 | — |
| DAO | 0.621 | 0.406 | — |
| LSM2 | 0.608 | 0.608 | — |
| FDX2 | 0.606 | 0.336 | — |
| FADS6 | 0.569 | 0.000 | — |
| GLDC | 0.558 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dmel\CG1503 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| RpS20 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Pgd | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Mettl1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| "EG:65F1.1" | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| "l | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| mtDNA-helicase | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| UPRT | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NIPSNAP2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PpD3 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.7 + PDB: 6ZK7, 8ORJ | pLDDT=88.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytosol; Cytoplasm, myofibril, / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PYROXD1 — tRNA ligase complex-associated NAD(P)H dehydrogenase PYROXD1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小500 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WU10
- Protein Atlas: https://www.proteinatlas.org/ENSG00000121350-PYROXD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PYROXD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WU10
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000121350-PYROXD1/subcellular

![](https://images.proteinatlas.org/38320/580_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/38320/580_C12_2_red_green.jpg)
![](https://images.proteinatlas.org/38320/590_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/38320/590_C12_2_red_green.jpg)
![](https://images.proteinatlas.org/38320/967_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/38320/967_A12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WU10-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
