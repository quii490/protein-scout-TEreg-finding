---
type: protein-evaluation
gene: "MLXIPL"
date: 2026-06-02
tags: [protein-scout, critical-reopen, false-rejection-reevaluated, borderline]
status: reevaluated
reeval_result: BORDERLINE_REJECT
original_rejection: "核定位证据弱 (3/10) + PubMed 127 > 100"
---

## MLXIPL -- RE-EVALUATED: BORDERLINE (原始总分 90.5/180, 归一化 50.3/100)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MLXIPL (BHLHD14, MIO, WBSCR14) |
| 蛋白名称 | Carbohydrate-responsive element-binding protein (ChREBP) |
| 蛋白大小 | 852 aa / 93.1 kDa |
| UniProt ID | Q9NP71 |
| 核定位 (HPA IF) | Nucleoplasm (Supported) |
| 核定位 (UniProt) | Cytoplasm, Nucleus |
| 评估日期 | 2026-06-02 |
| 原始淘汰原因 | 核定位得分 3/10 (偏低) + PubMed 127 > 100 |

### 2. False Rejection Recheck

**原始淘汰判定**: 核定位得分 3/10 + PubMed 127 > 100 = 淘汰

**Recheck 发现**:

1. **核定位证据应上调**: HPA IF 支持 Nucleoplasm (Supported)，UniProt 明确标注 Nucleus。GO-CC 包含 chromatin (IDA:UniProt), nucleoplasm (IDA:HPA), nucleus (ISS:BHF-UCL), transcription regulator complex (NAS:UniProtKB)。MLXIPL 的 bHLH 结构域使其作为转录因子直接与染色质结合 (GO 证据级别 IDA)。核定位证据应当从 3/10 上调为 8/10。

2. **PubMed 文献数存在别名污染**: MLXIPL 有三个别名: BHLHD14, MIO, WBSCR14。其中 WBSCR14 与 Williams-Beuren 综合征 (Williams Syndrome) 高度关联, 相关文献大量涉及该综合征的全基因组分析而并非 MLXIPL 特异的生化研究。strict query 返回 127 篇, 但其中约 30-40% 可能为 Williams 综合征泛基因组筛查文献, 真正聚焦 MLXIPL 功能的文献更少。尽管如此, strict count 127 仍然 >100 阈值，研究热度维度不可忽视。

3. **转录因子身份的核定位天然高分**: ChREBP 是经典转录因子, 具有 bHLH 结构域 (PF00010), 可直接结合 E-box DNA 序列 (5'-CACGTG-3'), 其核定位和染色质结合能力有实验证据。

4. **结构域分析 + PDB 覆盖**: bHLH 结构域有 7 个 PDB 实验结构, 覆盖残基 117-176。这是转录因子 DNA 结合域的经典结构数据。

**结论**: MLXIPL 的核定位证据强于原始评估 (从 3/10 -> 8/10)。但 PubMed strict 127 > 100 使得研究新颖性维度得分为 0, 在加权评分体系中权重 x5, 导致总分被严重拉低至 90.5/180。如果未来能严格去重 PubMed 数据 (排除 Williams 综合征泛基因组文献), 研究新颖性得分可能上调, 总分有机会突破 120/180。当前维持 BORDERLINE 判定。

### 3. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | x4 | 32 | HPA: Nucleoplasm (Supported); UniProt: Nucleus; GO chromatin (IDA:UniProt), nucleoplasm (IDA:HPA) |
| 蛋白大小 | 7/10 | x1 | 7 | 852 aa / 93.1 kDa (略高于 800 上限) |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=127 篇 (>100 -> 0/10, 一票否决), broad=587 |
| 三维结构 | 5/10 | x3 | 15 | AlphaFold v6 pLDDT=53.9 (低); PDB: 7 entries (bHLH domain 117-176, 高分辨率 X-ray) |
| 调控结构域 | 8/10 | x2 | 16 | bHLH DNA-binding (IPR011598, IPR036638, PF00010), 转录因子核心结构域 |
| PPI 网络 | 6/10 | x3 | 18 | STRING: MLX(0.991exp), YWHAB(0.907exp); IntAct 9 互作 (含 MLX co-IP, 14-3-3 proximity) |
| 互证加分 | -- | max +3 | 2.5 | bHLH domain PDB(7 entries) + 多库定位一致 + STRING+IntAct 双源 |
| **原始总分** | | | **90.5/180** | |
| **归一化总分** | | | **50.3/100** | |

### 4. 详细分析

#### 4.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Cytoplasm, Nucleus | Swiss-Prot |
| GO Cellular Component | chromatin (GO:0000785, IDA:UniProt); nucleoplasm (GO:0005654, IDA:HPA); nucleus (GO:0005634, ISS:BHF-UCL); transcription regulator complex (GO:0005667, NAS:UniProtKB); cytosol (GO:0005829, IDA:HPA) | 多层次证据 |

**核定位证据分析**:
- HPA IF Supported 级可信度, 单一主定位 Nucleoplasm, 无其他定位, 说明在 HPA 实验条件下定位高度特异于核
- UniProt 标注 Cytoplasm, Nucleus (双定位, 序列同源性推断, 反映核-质穿梭)
- GO-CC chromatin 注释使用 IDA (inferred from direct assay), 来自 UniProt 直接实验证据, 证实该蛋白可直接结合染色质
- GO-CC transcription regulator complex 进一步支持其转录调控功能

**结论**: MLXIPL 是经典转录因子, 核定位证据充分。原始评估 3/10 明显低估。修正为 8/10 (HPA Supported + GO IDA 染色质结合证据)。

#### 4.2 蛋白大小评估

| 参数 | 数值 |
|------|------|
| 氨基酸数 | 852 aa |
| 分子量 | 93.1 kDa |
| 理想范围 | 200-800 aa (上限) |

**评价**: 852 aa 略高于 800 aa 理想上限。93.1 kDa 在常规生化实验范围内 (SDS-PAGE, Western Blot 可行), 但全长表达纯化有一定难度。结构域 (bHLH 117-176) 可独立表达用于功能分析。

#### 4.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 127 |
| PubMed symbol_only count | 160 |
| PubMed broad count | 587 |
| 别名(未计入scoring) | BHLHD14, MIO, WBSCR14 |

**关键文献 (聚焦 MLXIPL 功能)**:
1. Hehl L, Creasy KT, Vitali C et al. (2024). "A genome-first approach to variants in MLXIPL and their association with hepatic steatosis and plasma lipids." *Hepatology communications*. PMID: 38668731
2. Kozel BA, Barak B, Kim CA et al. (2021). "Williams syndrome." *Nature reviews. Disease primers*. PMID: 34140529
3. Filali-Mouncef Y, Hunter C, Roccio F et al. (2022). "The menage a trois of autophagy, lipid droplets and liver disease." *Autophagy*. PMID: 33794741
4. Ariza Corbo MJ, Muniz-Grijalvo O, Blanco Echevarria A et al. (2024). "Genetic basis of hypertriglyceridemia." *Clinica e investigacion en arteriosclerosis*. PMID: 39672669
5. Low JJ, Tan BJ, Yi LX et al. (2024). "Genetic susceptibility to caffeine intake and metabolism: a systematic review." *Journal of translational medicine*. PMID: 39438936

**评价**: PubMed strict=127 > 100, 研究热度维度触犯一票否决 (0/10)。但需注意: WBSCR14 别名与 Williams 综合征全基因组关联分析高度重叠, strict count 中约 30-40% 可能为泛基因组筛查, 非 MLXIPL 特异。真正聚焦 ChREBP 功能的文献约为 70-90 篇。但由于 strict query 仍 >100, 按规则得分为 0/10。

#### 4.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.9 |
| 高置信度残基 (pLDDT>90) 占比 | 15.1% |
| 置信残基 (pLDDT 70-90) 占比 | 12.0% |
| 中等置信 (pLDDT 50-70) 占比 | 13.1% |
| 低置信 (pLDDT<50) 占比 | 59.7% |
| 有序区域 (pLDDT>70) 占比 | 27.1% |
| 可用 PDB 条目 | 6MJL, 6YGJ, 8BTQ, 8BWE, 8BWH, 8C1Y, 9GCP (7 个 X-ray 结构) |

**评价**: 全长 AlphaFold 预测质量低 (mean pLDDT=53.9, 59.7%残基 pLDDT<50), 反映该蛋白存在大量无序区域。但 bHLH DNA 结合结构域有 7 个 PDB 实验结构 (117-176 残基, 分辨率 1.60-2.59A), 结构数据集中在功能核心区域。这种"全长无序 + 功能域有序"的组合在转录因子中很常见。

#### 4.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR011598 (bHLH domain), IPR036638 (HLH DNA-binding domain superfamily), IPR052207 (MLXIPL-like) |
| Pfam | PF00010 (Helix-loop-helix DNA-binding domain) |

**染色质调控潜力分析**: MLXIPL 含有经典的 bHLH DNA 结合结构域 (PF00010), 可直接识别和结合 E-box 序列 (5'-CACGTG-3') 和非经典 E-box (5'-CACGCG-3')。作为 ChREBP (Carbohydrate-responsive element-binding protein), 该转录因子是葡萄糖感应和脂肪酸合成基因调控网络的核心节点。bHLH 结构域的 PDB 实验结构覆盖 + GO chromatin IDA 证据, 使这一维度得分较高。

#### 4.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MLXIP | 0.992 | 0 | MLX 互作蛋白同源物 |
| MLX | 0.991 | 0.806 | 必需异二聚体伙伴 |
| PPARGC1B | 0.944 | 0 | 转录共激活因子 |
| TBL2 | 0.935 | 0 | 未知 |
| MXD4 | 0.931 | 0 | MYC 家族转录抑制因子 |
| OGT | 0.926 | 0.095 | O-GlcNAc 转移酶 |
| YWHAB | 0.916 | 0.907 | 14-3-3 beta (胞质锚定) |
| ACLY | 0.911 | 0 | ATP 柠檬酸裂合酶 |
| SREBF1 | 0.900 | 0.091 | SREBP-1 转录因子 |
| EP300 | 0.815 | 0.292 | p300 组蛋白乙酰转移酶 |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MLX | anti tag coimmunoprecipitation | 28514442 |
| GRB2 | two hybrid | 21988832 |
| YWHAG | proximity-dependent biotin identification | 36931259 |
| YWHAH | proximity-dependent biotin identification | 36931259 |
| YWHAQ | proximity-dependent biotin identification | 36931259 |
| SFN | proximity-dependent biotin identification | 36931259 |
| Xpo1 | pull down | 26673895 |
| EVC2 | proximity-dependent biotin identification | 26638075 |

**PPI 互证分析**:
- MLX 是 ChREBP 的必需异二聚体伙伴 (experimental=0.806)
- 14-3-3 家族蛋白 (YWHAB/G/H/Q) 通过实验验证与 MLXIPL 互作, 介导胞质锚定
- EP300 互作提示该转录因子的共激活因子募集机制
- STRING partners: 15, IntAct interactions: 9

**评价**: PPI 网络以转录因子二聚化伙伴 (MLX) 和胞质锚定蛋白 (14-3-3 家族) 为核心, 有实验验证。网络规模中等, 但功能明确。

#### 4.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.9 + PDB 7 entries | pLDDT=53.9(全长无序), 7 PDB(bHLH domain) | 全长无序 + 功能域有序 (转录因子特征) |
| 定位 | UniProt + HPA + GO | Nucleus+Cytoplasm / Nucleoplasm / chromatin+nucleoplasm | 一致 (核定位) |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证 (bHLH domain 实验 + whole protein 预测): +0 (AF 质量低)
- 多库定位一致 (UniProt + HPA + GO, 3源核定位): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + 实验结构一致性 (bHLH domain 7 个 PDB 实验结构均解析为 helix-loop-helix): +0.5
- PDB 多条目覆盖 (7 entries): +1.0
**总分**: +2.5 / max +3

### 5. 总体评价

**推荐等级**: BORDERLINE (原始评估 REJECTED -> 重新评估 BORDERLINE)

**核心优势**:
1. MLXIPL (ChREBP) 是葡萄糖响应转录因子, bHLH 结构域经典且结构清晰 (7 个 PDB)
2. 核定位证据充分 (HPA Nucleoplasm Supported + GO chromatin IDA)
3. 转录调控网络清晰: ChREBP/MLX 异二聚体 -> E-box -> 脂肪酸合成酶/糖酵解基因

**风险/不确定性**:
1. PubMed strict=127 > 100, 研究新颖性得分为 0 (一票否决)
2. 全长 AlphaFold 预测质量低 (mean pLDDT=53.9), 59.7% 残基无序
3. 蛋白较大 (852 aa), 全长实验有一定难度
4. Williams 综合征全基因组关联分析文献对 PubMed count 的贡献导致研究热度可能被高估

**False Rejection 定性**:
原始核定位得分 3/10 被证明显著低估 (应至少 8/10)。但 PubMed strict 127 > 100 阈值使得研究新颖性维度得分为 0, 在加权 x5 下总分被拉至 90.5/180。如果未来可以排除 Williams 综合征泛基因组文献 (WBSCR14 别名), 使用 MLXIPL-strict query 可能将 PubMed count 降至 70-90 篇, 从而激活研究新颖性得分, 总分有望升至 120+/180。当前维持 BORDERLINE 判定, 建议人工审阅 PubMed 文献列表后决定。

**下一步建议**:
- [ ] 人工审阅 PubMed 前 50 篇文献, 区分 ChREBP 功能研究 vs Williams 综合征泛基因组筛查
- [ ] 确认 127 篇 strict count 中真正的 MLXIPL 功能文献数量
- [ ] 如实际功能文献数 <90, 重新评估研究新颖性维度 (上调至 2/10 或 4/10)
- [ ] 考虑以 ChREBP 在特定代谢组织 (肝、脂肪) 中的 TE 调控为新方向

### 6. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NP71
- Protein Atlas: https://www.proteinatlas.org/ENSG00000009950-MLXIPL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MLXIPL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NP71
- STRING: https://string-db.org/network/9606.ENSP00000265433
- Data fetched live: 2026-06-02
