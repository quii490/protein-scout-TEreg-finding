---
type: protein-evaluation
gene: "CEP162"
date: 2026-06-01
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CEP162 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | CEP162 / C6orf84, KIAA1009, QN1 |
| 蛋白大小 | 1403 aa / 161.9 kDa |
| UniProt ID | Q5TB80 (CE162_HUMAN) |
| 评估日期 | 2026-06-01 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | HPA Approved: Nucleoplasm + Cytosol 双主定位; UniProt: Nucleus + 中心体/中心粒; 核质双分布 |
| 📏 蛋白大小 | 5/10 | ×1 | 5.0 | 1403 aa, 1200–2000 aa 范围 |
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed strict=11 (\≤20 → 10分) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18.0 | AF mean pLDDT=62.9; 无PDB实验结构; 新颖蛋白基线 |
| 🧬 调控结构域 | 7/10 | ×2 | 14.0 | 无注释结构域; 新颖蛋白基线(\≤100 PubMed) |
| 🔗 PPI | 6/10 | ×3 | 18.0 | IntAct co-IP/cross-linking物理互作; STRING实验得分0.3–0.6; 伴侣以中心体/纤毛为主, 染色质调控有限 |
| **加权总分** | | | **121/180**** |
| **归一化总分 (÷1.83)** | | | **66.1/100**** |  |

> 互证加分: +1 (HPA+UniProt 核信号一致; STRING+IntAct KCTD8重叠; 无PDB; 无domain交叉验证)

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | Nucleoplasm, Cytosol (双主定位) | Approved |
| UniProt | Cytoplasm, Cytoskeleton, Centrosome, Centriole, Spindle, Nucleus | Reviewed |
| GO-CC | nucleoplasm (IDA:HPA), cytosol (IDA:HPA), centriole (IDA), centrosome (IDA), axonemal microtubule (IDA), centriolar satellite (IDA:HPA), ciliary basal body (IDA:HPA), Golgi apparatus (IDA:HPA), spindle (IEA), sperm head-tail coupling apparatus (IDA:HPA), sperm midpiece (IDA:HPA), sperm principal piece (IDA:HPA) | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/CEP162/IF_images/CEP162_A-431_38.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/CEP162/IF_images/CEP162_A-431_47.jpg|A-431]]

**结论**: CEP162 在 HPA 中以 Nucleoplasm 和 Cytosol 作为双主定位 (Approved 级别), 另外在 Centriolar satellite、Basal body、Connecting piece、Mid piece、Principal piece 中也有额外观测。UniProt 列出 Nucleus 与 Centrosome/Centriole/Spindle 等多重定位。GO-CC 的 nucleoplasm 注释来自 IDA:HPA, 可信度较高。蛋白主要在中心体/初级纤毛行使功能, 但同时被多个数据库确认存在核定位信号。核定位得分 4 分 (核质双分布且非专一核蛋白)。

#### 3.2 蛋白大小评估
1403 aa, 161.9 kDa, 处于 1200–2000 aa 的理想范围。大蛋白可能具有多结构域、多互作位点。**评价**: 5 分 (1200–2000 aa范围内)。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict 计数 | 11 |
| PubMed symbol-only | 15 |
| PubMed broad | 16 |
| 最早发表年份 | 2013 (Wang WJ et al., Nature Cell Biology) |

**关键文献 (Top 5)**:
1. **Wang WJ et al. (2013)**. "CEP162 is an axoneme-recognition protein promoting ciliary transition zone assembly at the cilia base." *Nature Cell Biology*. PMID: 23644468 — 首次鉴定 CEP162 为纤毛过渡区组装的关键因子, 发现其直接识别并结合轴丝微管。
2. **Nuzhat N et al. (2023)**. "CEP162 deficiency causes human retinal degeneration and reveals a dual role in ciliogenesis and neurogenesis." *J Clin Invest*. PMID: 36862503 — 发现 CEP162 缺陷导致人类视网膜变性, 揭示其在纤毛发生和神经发生中的双重角色。
3. **Wu Z et al. (2024)**. "Cep131-Cep162 and Cby-Fam92 complexes cooperatively maintain Cep290 at the basal body." *PLoS Biology*. PMID: 38442096 — 阐明 Cep131-Cep162 复合体协同维持 Cep290 在基体定位的机制。
4. **Yin J et al. (2025)**. "CEP162: A critical regulator of ciliary transition zone assembly and its implications in ciliopathies." *J Cell Commun Signal*. PMID: 40270641 — 最新综述, 系统总结 CEP162 在纤毛病中的作用。
5. **Li H et al. (2023)**. "The association of five polymorphisms with diabetic retinopathy in a Chinese population." *Ophthalmic Genet*. PMID: 37066695 — CEP162 多态性与糖尿病视网膜病变的关联研究。

**评价**: 仅 11 篇 strict 文献, 高度新颖。主要研究集中在纤毛过渡区组装和纤毛病方向; 核定位虽有 GO 注释和 HPA 实验证据, 但文献中尚无核功能相关研究。新颖性 10 分 (\≤20, 直给 10)。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 62.9 |
| PDB 实验结构 | 无 |
| >90% (very high) | 20.4% |
| 70–90% (confident) | 28.1% |
| 50–70% (low) | 10.0% |
| <50% (very low) | 41.6% |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/CEP162/CEP162-PAE.png]]

**评价**: AlphaFold 预测质量中等 (pLDDT 62.9)。约 48.5% 的残基有可靠预测 (pLDDT>70), 其中 20.4% 为极高置信度 (>90%)。但仍有 41.6% 残基预测置信度很低 (<50%), 提示蛋白含有大量无序区域。无 PDB 实验结构。对 PubMed ≤100 篇的新颖蛋白, 结构得分基线 = 6。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| InterPro | IPR038774 |
| Pfam | 无 |
| UniProt | 无domain注释 |

**染色质调控潜力分析**: InterPro 检出 IPR038774, 但无 Pfam 结构域注释。无经典 DNA-binding、chromatin-binding 或转录调控结构域。蛋白功能注释为纤毛过渡区组装的轴丝微管识别蛋白, 主要定位于中心体/中心粒远端, 其已知功能远离染色质调控。对 PubMed ≤100 篇的新颖蛋白, 结构域得分基线 = 7。

#### 3.6 PPI 网络（四源综合）

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|
| KCTD8 | anti tag co-IP | 28514442 | K+ channel tetramerization domain | ❌ |
| CCDC47 | cross-linking | 30021884 | Coiled-coil domain, ER protein | ❌ |
| FLNA | anti tag co-IP | 26496610 | Filamin A, actin cross-linking | ❌ |
| DISC1 | two hybrid | 31413325 | Disrupted in schizophrenia 1, scaffold | ❌ |
| LXN | anti bait co-IP | 17353931 | Latexin, carboxypeptidase inhibitor | ❌ |
| CAPN6 | anti tag co-IP | 28514442 | Calpain 6, microtubule stabilization | ❌ |
| SYBU | anti tag co-IP | 28514442 | Syntabulin, syntaxin binding | ❌ |

**STRING 预测互作** / **文献实验互作**:

| Partner | 证据 | 功能类别 | 调控相关？ |
|---|---|---|---|
| CEP290 | STRING 0.885 (exp=0.512) | 中心体/纤毛蛋白, ciliopathy gene | ❌ |
| TUBG1 | STRING 0.778 (exp=0) | Gamma-tubulin, 微管成核 | ❌ |
| CEP120 | STRING 0.691 (exp=0.292) + UniProt 6 experiments | 中心体蛋白, centriole duplication | ❌ |
| KIAA0753 | STRING 0.684 (exp=0.292) | 中心体/纤毛蛋白 | ❌ |
| CCP110 | STRING 0.661 (exp=0.292) | Centriolar coiled-coil protein, ciliogenesis | ❌ |
| IQCB1 | STRING 0.650 (exp=0.292) | IQ calmodulin-binding, ciliopathy | ❌ |
| CEP135 | STRING 0.648 (exp=0.337) + UniProt 3 experiments | 中心体蛋白 | ❌ |
| HAUS1 | STRING 0.646 (exp=0.292) | Augmin complex, spindle | ❌ |
| HAUS4 | STRING 0.638 (exp=0.292) | Augmin complex, spindle | ❌ |
| YEATS4 | STRING 0.636 (exp=0.230) | YEATS domain, chromatin reader (NuA4 HAT) | **是** |
| HAUS6 | STRING 0.628 (exp=0.089) | Augmin complex, spindle | ❌ |
| CEP97 | STRING 0.597 (exp=0.292) | 中心体蛋白, ciliogenesis suppressor | ❌ |
| TCTN1 | STRING 0.592 (exp=0) | Tectonic-1, ciliary transition zone | ❌ |
| CEP128 | STRING 0.591 (exp=0.292) | 中心体蛋白 | ❌ |
| KCTD8 | STRING 0.574 (exp=0.574) + IntAct co-IP | K+ channel tetramerization | ❌ |

**已知复合体成员** (GO Cellular Component):
- Centriole (GO:0005814) — IDA
- Centrosome (GO:0005813) — IDA
- Ciliary basal body (GO:0036064) — IDA:HPA
- Axonemal microtubule (GO:0005879) — IDA
- Nucleoplasm (GO:0005654) — IDA:HPA
- Spindle (GO:0005819) — IEA
- Sperm head-tail coupling apparatus (GO:0140611) — IDA:HPA
- Centriolar satellite (GO:0034451) — IDA:HPA

**调控相关比例**: 1/22 (4.5%) — 仅 YEATS4 为染色质调控蛋白 (NuA4 HAT 复合体中的 chromatin reader); 其余 21 个伴侣均为中心体/纤毛/纺锤体/细胞骨架相关蛋白。GO-CC 中无 chromatin/transcription complex 注释。

**PPI 互证**: 
- STRING+IntAct 重叠: KCTD8 — 两源一致确认 ✓
- UniProt STRING 重叠: CEP120 (6 experiments, STRING 0.691), CEP135 (3 experiments, STRING 0.648), CEP290 (7 experiments, STRING 0.885) — 多源一致确认 ✓
- IntAct 实验互作 (co-IP/cross-linking) 均为非调控蛋白
- 仅一个染色质调控伴侣 (YEATS4), 且仅来自 STRING 预测

**评价**: PPI 网络高度集中于中心体/纤毛生物学功能。IntAct 实验互作经过 co-IP 和 cross-linking 验证, 可信度良好, 但均为结构/骨架相关蛋白。STRING 预测网络中, 实验得分最高 (0.512) 的 CEP290 是已知的核心纤毛蛋白, 与 CEP162 在基体处的功能协同有文献支持 (Wu et al. 2024)。唯一染色质调控相关伴侣 YEATS4 的 STRING 实验得分仅 0.230。总体而言, PPI 网络几乎不支持该蛋白参与染色质调控。PPI 得分 6。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 核定位 | HPA (Approved: Nucleoplasm+Cytosol) / UniProt (Nucleus+Centrosome) | 两源均确认核信号 | 一致 ✓ |
| 三维结构 | AlphaFold pLDDT=62.9 | 中等置信度, 部分有序, 无PDB | 部分 |
| 结构域 | InterPro (IPR038774) / UniProt (无) | InterPro有检出但无Pfam注释, UniProt无 | 部分 |
| PPI | STRING + IntAct | KCTD8两源重叠; CEP120/135/290多源一致; 无调控相关重叠 | 部分 |

**互证加分明细**:
- 定位互证: HPA (Approved) + UniProt (Nucleus) → ≥2来源确认核信号 → **+0.5**
- PPI互证: STRING+IntAct 有 KCTD8 重叠; STRING+UniProt 有 CEP120/135/290 重叠 → 多源实验验证一致 → **+0.5**
- 无PDB实验结构互证
- 无domain跨库互证

**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**核心优势**:
1. **高度新颖**: PubMed strict 仅 11 篇, 几乎未被充分研究
2. **纤毛生物学核心因子**: 在初级纤毛过渡区组装中作为轴丝微管识别蛋白, 功能机制明确
3. **人类疾病关联**: 与视网膜变性 (Nuzhat 2023)、糖尿病视网膜病变 (Li 2023)、纤毛病 (Yin 2025) 直接相关
4. **多源确认核定位**: HPA Approved + UniProt + GO-CC 共同确认核质定位
5. **蛋白大 (1403 aa)**: 具有多结构域潜力

**风险/不确定性**:
1. **核功能完全未知**: 虽然多库确认核定位, 但 11 篇文献无一涉及核功能研究 — 核定位是真实信号还是旁路效应不确定
2. **PPI 网络不支持染色质调控**: 22 个伴侣中仅 1 个染色质调控蛋白 (YEATS4, 且仅来自 STRING 预测)
3. **无经典调控结构域**: InterPro/Pfam/UniProt 均无染色质/DNA 结合域注释
4. **研究赛道狭窄**: 所有文献均聚焦纤毛/中心体, TE 调控方向无任何先例, 从头探索风险极高

**下一步建议**:
- [ ] 验证 HPA 核定位信号的可靠性 — 使用独立抗体做 IF 确认
- [ ] 检查 CEP162 是否包含 NLS (核定位信号) — 序列分析
- [ ] 考虑 ChIP-seq 预处理实验以探测可能的染色质结合, 但预期收益较低 (PPI 网络不支持)
- [ ] 如核定位被确认非特异性, 建议降级为 rejected

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5TB80
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166532-CEP162
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CEP162
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5TB80
- STRING: https://string-db.org/
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q5TB80/
- IntAct: https://www.ebi.ac.uk/intact/


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| CEP290 | STRING | score=0.885, exp=0.512 |
| TUBG1 | STRING | score=0.778, exp=0 |
| CEP120 | STRING | score=0.691, exp=0.292 |
| KIAA0753 | STRING | score=0.684, exp=0.292 |
| CCP110 | STRING | score=0.661, exp=0.292 |
| Mer | IntAct | psi-mi:"MI:0399"(two hybrid fragment poo PMID:pubmed:15710747|imex:IM-16519| |
| ctp | IntAct | psi-mi:"MI:0018"(two hybrid) PMID:pubmed:14605208|imex:IM-16524| |
| LXN | IntAct | psi-mi:"MI:0006"(anti bait coimmunopreci PMID:pubmed:17353931 |

IntAct 有限记录。无 BioGrid 补充数据。

![[CEP162-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。

HPA IF 图像已本地嵌入。



PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/CEP162/CEP162-PAE.png]]


