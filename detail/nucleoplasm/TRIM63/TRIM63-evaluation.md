---
type: protein-evaluation
gene: "TRIM63"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TRIM63 — REJECTED (研究热度过高 (PubMed strict=180，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRIM63 / IRF, MURF1, RNF28, SMRZ |
| 蛋白名称 | E3 ubiquitin-protein ligase TRIM63 |
| 蛋白大小 | 353 aa / 40.2 kDa |
| UniProt ID | Q969Q1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus; Cytoplasm, myofibril, sarcomere, M line; |
| 蛋白大小 | 10/10 | ×1 | 10 | 353 aa / 40.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=180 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=82.8; PDB: 2D8U, 3DDT, 4M3L |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR017903, IPR050617, IPR042667, IPR027370, IPR000 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus; Cytoplasm, myofibril, sarcomere, M line; Cytoplasm, myofibril, sarcomere, Z line | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- M band (GO:0031430)
- microtubule (GO:0005874)
- nucleus (GO:0005634)
- Z disc (GO:0030018)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 180 |
| PubMed broad count | 864 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IRF, MURF1, RNF28, SMRZ |

**关键文献**:
1. Nonsyndromic Hypertrophic Cardiomyopathy Overview.. **. PMID: 20301725
2. Exogenous Nucleotides Supplementation Attenuates Age-Related Sarcopenia.. *Journal of cachexia, sarcopenia and muscle*. PMID: 40745399
3. Sepsis induces interleukin 6, gp130/JAK2/STAT3, and muscle wasting.. *Journal of cachexia, sarcopenia and muscle*. PMID: 34821076
4. CARM1 drives mitophagy and autophagy flux during fasting-induced skeletal muscle atrophy.. *Autophagy*. PMID: 38018843
5. Genes Associated With Hypertrophic Cardiomyopathy: A Reappraisal by the ClinGen Hereditary Cardiovascular Disease Gene Curation Expert Panel.. *Journal of the American College of Cardiology*. PMID: 39971408

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.8 |
| 高置信度残基 (pLDDT>90) 占比 | 57.2% |
| 置信残基 (pLDDT 70-90) 占比 | 24.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.4% |
| 低置信 (pLDDT<50) 占比 | 13.3% |
| 有序区域 (pLDDT>70) 占比 | 81.3% |
| 可用 PDB 条目 | 2D8U, 3DDT, 4M3L |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2D8U, 3DDT, 4M3L）+ AlphaFold高质量预测（pLDDT=82.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017903, IPR050617, IPR042667, IPR027370, IPR000315; Pfam: PF00643, PF13445 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000363390.3 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| MYBPC2 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| SGCB | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| SNAPIN | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| LAMA2 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| TRIM54 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| TRIM55 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| TTN | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| SQSTM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31391242|imex:IM-25805| |
| DCAF8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31391242|imex:IM-25805| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.8 + PDB: 2D8U, 3DDT, 4M3L | pLDDT=82.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm, myofibril, sarcomer / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TRIM63 — E3 ubiquitin-protein ligase TRIM63，研究基础较多，新颖性有限。
2. 蛋白大小353 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 180 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 180 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q969Q1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000158022-TRIM63/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRIM63
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q969Q1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
