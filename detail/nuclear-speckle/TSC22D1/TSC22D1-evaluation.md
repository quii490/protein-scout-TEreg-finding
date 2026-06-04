---
type: protein-evaluation
gene: "TSC22D1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TSC22D1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TSC22D1 / KIAA1994, TGFB1I4, TSC22 |
| 蛋白名称 | TSC22 domain family protein 1 |
| 蛋白大小 | 1073 aa / 109.7 kDa |
| UniProt ID | Q15714 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; UniProt: Cytoplasm; Nucleus; Cell membrane; Cytoplasm; Nucleus; Mitoc |
| 蛋白大小 | 8/10 | ×1 | 8 | 1073 aa / 109.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=47 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=42.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000580, IPR047862; Pfam: PF01166 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies | Approved |
| UniProt | Cytoplasm; Nucleus; Cell membrane; Cytoplasm; Nucleus; Mitochondrion; Cytoplasm; Nucleus; Mitochondr... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 47 |
| PubMed broad count | 98 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1994, TGFB1I4, TSC22 |

**关键文献**:
1. Kinase interaction analysis predicts actions of the WNK-OSR1/SPAK pathway.. *Communications biology*. PMID: 40913030
2. TSC22D1 is a newly identified inhibitor of insulin secretion in pancreatic beta cells.. *The FEBS journal*. PMID: 40679946
3. The interplay between TGF-β-stimulated TSC22 domain family proteins regulates cell-cycle dynamics in medulloblastoma cells.. *Journal of cellular physiology*. PMID: 30912127
4. Antagonistic TSC22D1 variants control BRAF(E600)-induced senescence.. *The EMBO journal*. PMID: 21448135
5. TSC22D1 and PSAP predict clinical outcome of tamoxifen treatment in patients with recurrent breast cancer.. *Breast cancer research and treatment*. PMID: 18299979

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 42.5 |
| 高置信度残基 (pLDDT>90) 占比 | 4.6% |
| 置信残基 (pLDDT 70-90) 占比 | 3.4% |
| 中等置信 (pLDDT 50-70) 占比 | 6.1% |
| 低置信 (pLDDT<50) 占比 | 85.9% |
| 有序区域 (pLDDT>70) 占比 | 8.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=42.5），有序残基占 8.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000580, IPR047862; Pfam: PF01166 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NRBP1 | 0.891 | 0.829 | — |
| TSC22D4 | 0.821 | 0.722 | — |
| TSC22D3 | 0.816 | 0.786 | — |
| LDLRAD4 | 0.720 | 0.000 | — |
| CA10 | 0.622 | 0.609 | — |
| LHX4 | 0.616 | 0.071 | — |
| TGFB1 | 0.563 | 0.000 | — |
| LHX3 | 0.561 | 0.071 | — |
| SMAD4 | 0.503 | 0.059 | — |
| MYC | 0.500 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000397435.2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SETDB1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ASAH1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RGS1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| APLP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MAP3K12 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CORO2B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CCDC90B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SFXN1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RPS9 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=42.5 + PDB: 无 | pLDDT=42.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cell membrane; Cytoplasm; Nucl / Nucleoplasm, Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TSC22D1 — TSC22 domain family protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1073 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 47 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=42.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15714
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102804-TSC22D1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TSC22D1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15714
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
